import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""




def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(2) == True
  assert math_it_up.is_even(3) == False
  assert math_it_up.is_even(0) == True
  assert math_it_up.is_even(88120832) == True
  assert math_it_up.is_even(798875) == False


def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(0) == False
  assert math_it_up.is_odd(9872) == False
  assert math_it_up.is_odd(9803) == True
  assert math_it_up.is_odd(29087302) == False
  assert math_it_up.is_odd(80901) == True



def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([5, 7]) == 6
  assert math_it_up.mean([5, 4, 2, 9]) == 5
  assert math_it_up.mean([5, 7, 98, 2, 12]) == 24.8
  assert math_it_up.mean([2, 10, 9, 1, 5, 5]) == 5.333333333333333


def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([1, 2, 3, 4, 5, 6, 7, 8, 9,]) == 5
  assert math_it_up.median([1, 2, 3, 4, 5, 6, 8, 9]) == 4.5


def test_mode():
  """
  Tests for the `mode` function
  """
  assert math_it_up.mode([2, 2, 2, 3, 4, 5, 3, 2, 5, 4]) == [2]
  assert math_it_up.mode([1, 6, 7, 8, 5, 5, 3, 2, 6, 5, 9, 5, 5, 7]) == [5]
  assert math_it_up.mode([3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8]) == [3]