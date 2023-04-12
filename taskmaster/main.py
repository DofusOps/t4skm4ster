from src.config_parser import ConfigParser
from src.process_manager import ProcessManager
from src.logger import Logger
from src.control_shell import ControlShell


def main():
    config_file = "configs/config.yaml"
    log_file = "logs/logfile.log"

    config_parser = ConfigParser(config_file)
    process_manager = ProcessManager(config_parser.config_data)
    logger = Logger(log_file)
    control_shell = ControlShell(process_manager, config_parser, logger)

    control_shell.run()


if __name__ == "__main__":
    main()
