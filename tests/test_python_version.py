import sys

def test_python_version():
    assert sys.version_info[:2] in [(3, 10), (3, 11)], "Test failed: Python version is not 3.10 or 3.11!"
