import sys
import logging
from color_print import ColorPrint


class ControlShell:
    def __init__(self, process_manager, config_parser):
        self.process_manager = process_manager
        self.config_parser = config_parser

    def print_status(self):
        # Implement logic to display the status of all programs
        logging.info("Printing status")
        for program_name in self.config_parser.config_data:
            ColorPrint.print_pass(program_name + " is loaded.")
            if program_name in self.process_manager.processes:
                ColorPrint.print_pass(program_name + " is running.")
            else:
                ColorPrint.print_fail(program_name + " is not running.")

    def start_program(self, program_name):
        # Implement logic to start a program
        logging.info("Starting program: " + program_name)
        self.process_manager.start_process(program_name)

    def stop_program(self, program_name):
        # Implement logic to stop a program
        logging.info("Stopping program: " + program_name)
        self.process_manager.stop_process(program_name)

    def restart_program(self, program_name):
        # Implement logic to restart a program
        logging.info("Restarting program: " + program_name)
        self.process_manager.restart_process(program_name)

    def monitor_processes(self):
        # Implement logic to reload the config file
        self.process_manager.monitor_processes()

    def reload_config(self):
        # Implement logic to reload the config file
        logging.info("Reloading config")
        self.config_parser.reload_config()

    def exit_program(self):
        sys.exit()

    def run(self):
        while True:
            cmd = input('\033[1;32;40m taskmaster> \033[0m')

            if cmd == 'status':
                self.print_status()
            elif cmd.startswith('start '):
                program_name = cmd.split(' ')[1]
                self.start_program(program_name)
            elif cmd.startswith('stop '):
                program_name = cmd.split(' ')[1]
                self.stop_program(program_name)
            elif cmd.startswith('restart '):
                program_name = cmd.split(' ')[1]
                self.restart_program(program_name)
            elif cmd == 'reload':
                self.reload_config()
            elif cmd == 'help':
                print("Available commands: status, start <program>, stop <program>, restart <program>, reload, exit")
            elif cmd == 'monitor':
                self.monitor_processes()
            elif cmd in ['exit', 'quit']:
                self.exit_program()
            else:
                ColorPrint.print_fail("Unknown command:" + cmd + ".\n", "Type 'help' for a list of available commands.\n")
