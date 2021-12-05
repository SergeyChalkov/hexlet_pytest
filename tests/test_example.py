import pytest
from hexlet_pytest.example import reverse, STACK


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_stack():
    assert not STACK
    STACK.append(1)
    STACK.append(2)
    assert STACK.pop() == 2
    assert STACK.pop() == 1
    assert not STACK


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
