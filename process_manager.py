import subprocess
import time
from config_parser import ConfigParser

class ProcessManager:
    def __init__(self, config_data):
        self.config_data = config_data
        
        self.processes = {}

    def start_process(self, program_name):
        print("Starting process: " + program_name)
        program_config = self.config_data.get(program_name)
        if not program_config:
            print(f"Program {program_name} not found in the configuration.")
            return
        print(program_config['cmd'])
        numprocs = program_config.get('numprocs', 1)

        for i in range(numprocs):
            process = subprocess.Popen(
                program_config['cmd'],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                universal_newlines=True,
                start_new_session=True,
            )
            self.processes[program_name] = process
            print(f"Starting process: {program_name} (PID: {process.pid})")

    def stop_process(self, program_name):
        print("Stopping process: " + program_name)
        program_config = self.config_data.get(program_name)
        if not program_config:
            print(f"Program {program_name} not found in the configuration.")
            return
        print(self.processes)
        process = self.processes.get(program_name)
        if not process:
            print(f"Process {program_name} is not running.")
            return
        
        stopsignal = program_config.get('stopsignal', 'TERM')
        signal_value = getattr(subprocess, f'signal.SIG{stopsignal}', subprocess.signal.SIGTERM)

        process.send_signal(signal_value)

        stoptime = program_config.get('stoptime', 10)
        time.sleep(stoptime)

        if process.poll() is None:
            process.kill()

        del self.processes[program_name]
        print(f"Stopped process: {program_name}")

    def restart_process(self, program_name):
        # Implement process restarting logic here.
        print("Restarting process: " + program_name)
        self.start_process(program_name)
        self.stop_process(program_name)

    def monitor_processes(self):
        # Implement process monitoring and management logic here.
        print("Monitoring processes...")

        while True:
            for program_name, process in self.processes.items():
                if process.poll() is not None:
                    print(f"Process {program_name} (PID: {process.pid}) exited unexpectedly.")
                    self.restart_process(program_name)
            
            time.sleep(5)  # Adjust the monitoring interval as needed.

    # Add more methods as needed to manage processes.
