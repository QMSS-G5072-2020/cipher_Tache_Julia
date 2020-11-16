from cipher_jat2167 import __version__
from cipher_jat2167 import cipher_jat2167

def test_version():
    assert __version__ == "0.1.0"

def test_single_word(example):
    expected = "dnwg"
    actual = cipher(example, 2)
    assert actual == expected
    if actual == expected: 
        return expected

test_single_word("blue")