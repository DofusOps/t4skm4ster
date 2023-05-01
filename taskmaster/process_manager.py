import os
import time
import subprocess
from color_print import ColorPrint


class ProcessManager:
    def __init__(self, config_data):
        self.config_data = config_data
        self.programs = {}

        for program_name in self.config_data:
            config = self.config_data[program_name]
            if config.get('onstart', False):
                self.start_program(program_name)

    def start_process(self, program_config):
        process = subprocess.Popen(
            program_config['cmd'].split(),
            env=program_config.get('env', os.environ),
            stdout=program_config.get('stdout', subprocess.PIPE),
            stderr=program_config.get('stderr', subprocess.PIPE),
            stdin=subprocess.PIPE,
            universal_newlines=True,
            start_new_session=True,
        )
        return process

    def start_program(self, program_name):
        program_config = self.config_data.get(program_name)

        if not program_config:
            ColorPrint.print_fail(f"Program {program_name} not found in the configuration.")
            return

        if program_name in self.programs.keys():
            ColorPrint.print_fail(f"Program {program_name} is already running.")
            return

        ColorPrint.print_info("Starting program: " + program_name)

        numprocs = program_config.get('numprocs', 1)
        self.programs[program_name] = [None] * numprocs
        for i in range(numprocs):
            process = self.start_process(program_config)
            self.programs[program_name][i] = {"process": process, "restarted": 0}
            ColorPrint.print_pass(f"Starting process: {program_name} (PID: {process.pid})")

    def stop_process(self, process, program_config):
        try:
            pgid = os.getpgid(process.pid)
        except Exception:
            return

        stopsignal = program_config.get('stopsignal', 'TERM')
        signal_value = getattr(subprocess, f'signal.SIG{stopsignal}', subprocess.signal.SIGTERM)
        os.killpg(pgid, signal_value)

        stoptime = program_config.get('stoptime', 10)
        time.sleep(stoptime)

        if process.poll() is None:
            process.kill()

    def stop_program(self, program_name):
        program_config = self.config_data.get(program_name)

        if not program_config:
            ColorPrint.print_fail(f"Program {program_name} not found in the configuration.")
            return

        program = self.programs.get(program_name)
        if not program:
            ColorPrint.print_fail(f"Program {program_name} is not running.")
            return

        for process in program:
            self.stop_process(process["process"], program_config)

        del self.programs[program_name]
        ColorPrint.print_pass(f"Stopped program: {program_name}")

    def restart_process(self, process, program_config):
        self.stop_process(process, program_config)
        process = self.start_process(program_config)
        return process

    def restart_program(self, program_name):
        # Implement process restarting logic here.
        ColorPrint.print_info(f"Restarting program: {program_name}")
        self.stop_program(program_name)
        self.start_program(program_name)

    def monitor_processes(self):
        for program_name, program in self.programs.items():
            for process in program:
                exited = process["process"].poll()
                if exited:
                    ColorPrint.print_fail(f"Process {program_name} (PID: {process['process'].pid}) exited unexpectedly.")
                    program_config = self.config_data.get(program_name)

                    # Check restart config
                    restart_instruction = program_config.get("restart", "always")
                    max_restarts = program_config.get("restart_limit", 3)
                    expected_codes = program_config.get("expected", [0])

                    if (restart_instruction == "always" or
                            (restart_instruction == "onerror" and exited in expected_codes)):
                        if process["restarted"] < max_restarts:
                            ColorPrint.print_fail("Restarting...")
                            process["process"] = self.restart_process(process, program_config)
                            process["restarted"] += 1
                        else:
                            ColorPrint.print_fail("Process restarted too many times, aborting.")
                    else:
                        ColorPrint.print_fail("Leaving program exited.")
