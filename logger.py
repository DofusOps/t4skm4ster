import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = self.setup_logger()

    def setup_logger(self):
        print("Setting up logger")
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def log_event(self, event):
        self.logger.info(event)
