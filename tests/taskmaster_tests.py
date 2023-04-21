import pexpect
# import os


# Utils
def pspawn():
    return pexpect.spawn(
        "coverage run taskmaster/main.py",
        # env=dict(os.environ, COVERAGE_PROCESS_START='.coveragerc')
    )


# Tests
def test_status():
    taskmaster = pspawn()

    taskmaster.sendline("status")
    taskmaster.expect("proc1 is loaded")
    taskmaster.expect("proc1 is not running")

    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_startstop():
    taskmaster = pspawn()

    taskmaster.sendline("start proc1")
    taskmaster.expect("Starting process: proc1")

    taskmaster.sendline("stop proc1")
    taskmaster.expect("Stopping process: proc1")

    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_restart():
    taskmaster = pspawn()

    taskmaster.sendline("start proc1")
    taskmaster.expect("Starting process: proc1")

    taskmaster.sendline("restart proc1")
    taskmaster.expect("Stopping process: proc1")
    taskmaster.expect("Starting process: proc1")

    taskmaster.sendline("stop proc1")
    taskmaster.expect("Stopping process: proc1")

    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_reload():
    taskmaster = pspawn()

    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")

    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


def test_help():
    taskmaster = pspawn()

    taskmaster.sendline("help")
    taskmaster.expect("Available commands: status, start <program>, stop <program>, restart <program>, reload, exit")

    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)


# def test_monitor():
#     taskmaster = pspawn()

#     taskmaster.sendline("monitor")
#     taskmaster.expect("Available commands: status, start <program>, stop <program>, restart <program>, reload, exit")

#     taskmaster.sendline("exit")
#     taskmaster.expect(pexpect.EOF)


def test_invalid():
    taskmaster = pspawn()
    taskmaster.sendline("xxxxx")
    taskmaster.expect("Unknown command:xxxxx.")
    taskmaster.expect("Type 'help' for a list of available commands.")
    taskmaster.sendline("exit")
    taskmaster.expect(pexpect.EOF)
