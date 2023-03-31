import yaml

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        print("Loading config file: " + self.config_file)
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def reload_config(self):
        print("Reloading config file: " + self.config_file)
        self.config_data = self.load_config()

    # Add methods to access and validate specific configuration data.
