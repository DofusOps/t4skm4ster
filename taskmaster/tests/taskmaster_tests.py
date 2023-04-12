import pytest
import pexpect

MAIN_PY_PATH = "../main.py"

@pytest.fixture(scope="module")
def taskmaster():
    taskmaster = pexpect.spawn(f"python {MAIN_PY_PATH}")
    yield taskmaster
    taskmaster.terminate(force=True)

def test_reload(taskmaster):
    taskmaster = pexpect.spawn("python main.py")
    taskmaster.sendline("reload")
    taskmaster.expect("Config file loaded successfully")
    taskmaster.expect("Loading")
    taskmaster.sendline("exit")