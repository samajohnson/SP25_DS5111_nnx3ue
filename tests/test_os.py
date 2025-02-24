import sys
import platform

def test_os():
    assert platform.system().lower() == "linux", "Test failed: OS is not Linux!"
