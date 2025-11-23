import pytest
from task_2 import (find_unique)


def test_all_unique():
    assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_some_duplicates():
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]

def test_all_duplicates():
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_empty_list():
    assert find_unique([]) == []

def test_strings():
    assert find_unique(["a", "b", "a", "c", "d", "b"]) == ["c", "d"]

def test_mixed_types():
    assert find_unique([1, "1", 1, 2, "2"]) == [2, "2"]

@pytest.mark.parametrize("input_list,expected", [
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [2, 3]),
    (["a", "a", "b"], ["b"]),
])
def test_find_unique_parametrized(input_list, expected):
    assert find_unique(input_list) == expected