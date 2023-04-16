import os
import logging
from config_parser import ConfigParser
from process_manager import ProcessManager
from control_shell import ControlShell
import coverage


def main():
    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, "../configs/config.yaml")
    logfile = os.path.join(dirname, "../logs/logfile.log")

    logging.basicConfig(
        level=logging.INFO,
        filename=logfile,
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    config_parser = ConfigParser(config_file)
    process_manager = ProcessManager(config_parser.config_data)
    control_shell = ControlShell(process_manager, config_parser)

    control_shell.run()


if __name__ == "__main__":
    coverage.process_startup()
    main()
