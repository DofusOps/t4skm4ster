import pexpect
import os


def test_reload():
    taskmaster = pexpect.spawn("coverage run main.py", env=dict(os.environ) | {'COVERAGE_PROCESS_START': '.coveragerc'})
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")
    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_help():
    taskmaster = pexpect.spawn("coverage run main.py", env=dict(os.environ) | {'COVERAGE_PROCESS_START': '.coveragerc'})
    taskmaster.sendline("help")
    taskmaster.expect("Available commands: status, start <program>, stop <program>, restart <program>, reload, exit")
    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_invalid():
    taskmaster = pexpect.spawn("coverage run main.py", env=dict(os.environ) | {'COVERAGE_PROCESS_START': '.coveragerc'})
    taskmaster.sendline("xxxxx")
    taskmaster.expect("Unknown command:xxxxx.")
    taskmaster.expect("Type 'help' for a list of available commands.")
    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)
