import sys
sys.path.append('.')

import bin.sample_adder as adder

def test_adder():
    assert 5 == adder.add(2,3), "Adder failed with 2 + 3, expected 5"
