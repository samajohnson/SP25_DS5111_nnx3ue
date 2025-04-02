import sys

def test_python_version():  # Just a head's up that you'll need to update this test when you change validation.yaml
    assert sys.version_info[:2] in [(3, 10), (3, 11), (3,12)], "Test failed: Python version is not 3.10, 3.11, or 3.12!"


# not finding the test to check for OS
# never mind, you put it in a differnt file... no worries
