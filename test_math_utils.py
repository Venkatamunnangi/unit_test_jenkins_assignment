from math_utils import MathUtils
import pytest


def addition_test():
    assert MathUtils.addition(2, 3) == 5

def subtraction_test():
    assert MathUtils.subtract(5, 3) == 2

def multiplication_test():
    assert MathUtils.multiply(3, 5) == 15

def division_test():
    assert MathUtils.divide(6, 3) == 2.0

def divide_by_zero_test():
    assert MathUtils.divide(8, 0) == -1.0