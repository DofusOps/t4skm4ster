import pytest
import pexpect

def test_reload():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")
    taskmaster.sendline("exit")

def test_reload2():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")
    taskmaster.expect("Loading")
    taskmaster.sendline("exit")