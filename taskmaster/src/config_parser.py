import yaml
from src.color_print import ColorPrint

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        ColorPrint.print_info("Loading config file: " + self.config_file)
        with open(self.config_file, 'r') as file:
            ColorPrint.print_pass("Config file loaded successfully")
            return yaml.safe_load(file)

    def reload_config(self):
        ColorPrint.print_info("Reloading config file: " + self.config_file)
        self.config_data = self.load_config()

    # Add methods to access and validate specific configuration data.
