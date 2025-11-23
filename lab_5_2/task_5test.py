import pytest
from task_5 import combine_dicts


def test_no_overlap():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    expected = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert combine_dicts(dict1, dict2) == expected

def test_with_overlap():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    expected = {"a": 1, "b": 3, "c": 4}
    assert combine_dicts(dict1, dict2) == expected

def test_empty_first_dict():
    dict1 = {}
    dict2 = {"a": 1, "b": 2}
    assert combine_dicts(dict1, dict2) == {"a": 1, "b": 2}

def test_empty_second_dict():
    dict1 = {"a": 1, "b": 2}
    dict2 = {}
    assert combine_dicts(dict1, dict2) == {"a": 1, "b": 2}

def test_both_empty():
    assert combine_dicts({}, {}) == {}

def test_nested_dicts():
    dict1 = {"a": {"nested": 1}}
    dict2 = {"b": 2}
    result = combine_dicts(dict1, dict2)
    assert result == {"a": {"nested": 1}, "b": 2}

@pytest.mark.parametrize("dict1,dict2,expected", [
    ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
    ({"a": 1}, {"a": 2}, {"a": 2}),
    ({}, {"a": 1}, {"a": 1}),
    ({"a": 1}, {}, {"a": 1}),
    ({}, {}, {}),
])
def test_combine_dicts_parametrized(dict1, dict2, expected):
    assert combine_dicts(dict1, dict2) == expected