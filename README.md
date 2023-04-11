# taskmaster

1. Define the configuration format: Decide on the format of the configuration file that will be used to specify the processes to manage. This could be a simple text file or a more complex format like YAML or JSON.

2. Parse the configuration file: Use a library like ConfigParser, PyYAML, or json to read and parse the configuration file into a data structure that can be used to manage the processes.

3. Start and monitor the processes: Use the subprocess module to start and manage the processes specified in the configuration file. You can use the Popen function to start a process, and the communicate method to send input to and receive output from the process. Use the poll method to check if the process is still running, and restart it if necessary.

4. Implement logging and notifications: Use the logging module to log messages to a file or a console. You can also use third-party packages like sentry-sdk or twilio to send notifications via email, SMS, or other channels when a process fails or crashes.

5. Implement the daemonization process: Use the daemonize package or a similar package to daemonize the job control process, so that it runs as a background process and can be managed using standard Unix tools like systemctl or service.

Todo:

- [x] Number of processes\
- [ ] Stop processes when multiple\
- [ ] Autostart programs\
- [ ] Autorestart\
- [ ] Exit status\
- [ ] How long to wait before successfully started\
- [ ] Retry attempt\
- [x] Sig to stop\
- [x] How long to wait before killing\
- [ ] Opt for redirect for stdout / stderr\
- [x] Set environment var\
- [ ] Working dir for programs\
- [ ] Umask for programs\

to test : docker run -p 8080:80 -it -v ~/Documents/taskmaster/:/home python:latest bash
