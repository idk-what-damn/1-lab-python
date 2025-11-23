import pytest
from task_3 import is_palindrome


def test_palindrome_word():
    assert is_palindrome("radar") == True

def test_non_palindrome_word():
    assert is_palindrome("hello") == False

def test_palindrome_number():
    assert is_palindrome(12321) == True

def test_non_palindrome_number():
    assert is_palindrome(12345) == False

def test_single_character():
    assert is_palindrome("a") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_case_insensitive():
    assert is_palindrome("Racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("a man a plan a canal panama") == True

@pytest.mark.parametrize("word,expected", [
    ("madam", True),
    ("racecar", True),
    ("hello", False),
    (12321, True),
    (12345, False),
    ("", True),
    ("A Santa at NASA", True),
])
def test_is_palindrome_parametrized(word, expected):
    assert is_palindrome(word) == expected