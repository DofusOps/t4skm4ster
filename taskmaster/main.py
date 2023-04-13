import os
import coverage
from config_parser import ConfigParser
from process_manager import ProcessManager
from logger import Logger
from control_shell import ControlShell


def main():
    coverage.process_startup()

    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, "../configs/config.yaml")
    log_file = os.path.join(dirname, "../logs/logfile.log")

    config_parser = ConfigParser(config_file)
    process_manager = ProcessManager(config_parser.config_data)
    logger = Logger(log_file)
    control_shell = ControlShell(process_manager, config_parser, logger)

    control_shell.run()


if __name__ == "__main__":
    main()
