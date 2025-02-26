import sys

def test_python_version():
    assert sys.version_info[:2] in [(3, 10), (3, 11), (3,12)], "Test failed: Python version is not 3.10, 3.11, or 3.12!"
