from math_utils import MathUtils
import pytest

def test_add():
    assert MathUtils.add(2, 3) == 5

def test_subtract():
    assert MathUtils.subtract(5, 3) == 2

def test_multiply():
    assert MathUtils.multiply(3, 5) == 15

def test_divide():
    assert MathUtils.divide(6, 3) == 2.0

def test_divide_by_zero():
    assert MathUtils.divide(8, 0) == -1.0