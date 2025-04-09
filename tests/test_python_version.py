import sys

def test_python_version():
    assert sys.version_info[:2] in [(3, 12), (3,13)], "Test failed: Python version is not 3.12, or 3.13!"
