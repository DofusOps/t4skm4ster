import configparser
import time
import logging
import subprocess

# Task master is a program of job control and task scheduling
# It is a daemon that runs in the background and controls the execution of other programs

config = configparser.ConfigParser()
config.read('config.ini')

# Parse the config file
processes = []
for section in config.sections():
    process = {
        'name': config[section]['name'],
        'command': config[section]['command'],
        'restart': config[section].getboolean('restart', True),
        'running': False,
        'proc': None,
    }
    processes.append(process)

# Set up logging
logging.basicConfig(filename='taskmaster.log', level=logging.DEBUG)

# Main loop
while True:
    for process in processes:
        if not process['running']:
            logging.info(f'Starting process {process["name"]}')
            process['running'] = True
            process['proc'] = subprocess.Popen(
                process['command'].split(),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        else:
            returncode = process['proc'].poll()
            if returncode is not None:
                if process['restart']:
                    logging.error(f'Process {process["name"]} exited with code {returncode}. Restarting...')
                    process['running'] = False
                else:
                    logging.error(f'Process {process["name"]} exited with code {returncode}. Not restarting.')
            else:
                logging.debug(f'Process {process["name"]} is still running.')
    time.sleep(1)

# When you run this program, you are able to type in the command line and enter the commands to control the processes.
    cmd = input('Enter a command: ')
    if cmd == 'exit':
        break
    elif cmd == 'status':
        for process in processes:
            print(f'{process["name"]}: {process["running"]}')
    elif cmd == 'restart':
        for process in processes:
            if process['running']:
                process['proc'].terminate()
                process['running'] = False
    else:
        print('Invalid command')
