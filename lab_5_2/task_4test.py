import pytest
from task_4 import are_anagrams


def test_anagrams():
    assert are_anagrams("listen", "silent") == True

def test_not_anagrams():
    assert are_anagrams("hello", "world") == False

def test_same_word():
    assert are_anagrams("test", "test") == True

def test_different_length():
    assert are_anagrams("test", "testing") == False

def test_case_insensitive():
    assert are_anagrams("Tea", "Eat") == True

def test_with_spaces():
    assert are_anagrams("school master", "the classroom") == True

def test_empty_strings():
    assert are_anagrams("", "") == True

def test_one_empty_string():
    assert are_anagrams("test", "") == False

@pytest.mark.parametrize("str1,str2,expected", [
    ("listen", "silent", True),
    ("hello", "world", False),
    ("tea", "eat", True),
    ("", "", True),
    ("test", "", False),
    ("Dormitory", "Dirty room", True),
])
def test_are_anagrams_parametrized(str1, str2, expected):
    assert are_anagrams(str1, str2) == expected