import configparser
import time
import logging
import subprocess

#Task master is a program of job control and task scheduling
#It is a daemon that runs in the background and controls the execution of other programs

config = configparser.ConfigParser()
config.read('config.ini')

# Parse the config file
process = []
for section in config.sections():
    process = {
        'name': config[section]['name'],
        'command': config[section]['command'],
        'interval': config[section]['interval'],
        'restart': config[section].getboolean('restart', True),
        'running': False,
    }
    process.append(process)

# Set up logging
logging.basicConfig(filename='taskmaster.log', level=logging.DEBUG)

# Main loop
while True:
    for process in process:
        if not process['running']:
            logging.info('Starting process: %s', process['name'])
            process['process'] = subprocess.Popen(process['command'])
            process['running'] = True
        else:
            if process['process'].poll() is not None:
                logging.info('Process %s has terminated', process['name'])
                if process['restart']:
                    logging.info('Restarting process: %s', process['name'])
                    process['process'] = subprocess.Popen(process['command'])
                else:
                    process['running'] = False
    time.sleep(1)