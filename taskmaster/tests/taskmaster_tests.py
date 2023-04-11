import pytest
import pexpect

def test_reload():
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")