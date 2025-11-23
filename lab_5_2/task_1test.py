import pytest
from task_1 import count_words


def test_normal_sentence():
    assert count_words("Hello world this is a test") == 6

def test_empty_string():
    assert count_words("") == 0

def test_only_spaces():
    assert count_words("     ") == 0

def test_single_word():
    assert count_words("Hello") == 1

def test_multiple_spaces():
    assert count_words("Hello    world   test") == 3

def test_with_punctuation():
    assert count_words("Hello, world! This is a test.") == 6

@pytest.mark.parametrize("sentence,expected", [
    ("", 0),
    ("hello", 1),
    ("hello world", 2),
    ("  multiple   spaces  ", 2),
])
def test_count_words_parametrized(sentence, expected):
    assert count_words(sentence) == expected