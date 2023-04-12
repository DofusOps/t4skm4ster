from time import sleep
import pexpect

def test_spawn():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.expect("Loading config file:")
    taskmaster.expect("Config file loaded successfully")
    taskmaster.expect("Setting up logger")


def test_help():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("help")
    taskmaster.expect("Available commands:")


def test_start():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("start proc2")
    taskmaster.expect("Starting process")
    taskmaster.expect("Started process")
    taskmaster.expect("PID")


# def test_stop():
#     taskmaster = pexpect.spawn("python main.py")
#     taskmaster.sendline("start proc2")
#     taskmaster.expect("Started process")
#     sleep(120)
#     taskmaster.sendline("stop proc2")
#     taskmaster.expect("Stopping process")
#     taskmaster.expect("Stopped process")
#     taskmaster.expect("PID")


# def test_restart():
#     taskmaster = pexpect.spawn("python main.py")
#     taskmaster.sendline("restart proc2")
#     taskmaster.expect("Restarting process")
#     taskmaster.expect("Stopped process")
#     taskmaster.expect("PID")
#     taskmaster.expect("Started process")
#     taskmaster.expect("PID")
#     taskmaster.expect("Restarted process")


# def test_status():


def test_reload():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")


# def test_exit():