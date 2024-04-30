import pytest
from count import * 
from factorial import *
from list_of_squares import *
from vowels import *

# part 1

def test_count_zeros():
	assert count([0,0,0],0)==3

def test_count_string():
	assert count(["a","a","a"],"a")==3

def test_count_minus():
	assert count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

# part 2

def test_factorial_zeros():
	assert fact(0) == 0

def test_factorial_zeros():
	assert fact(0) == 1

def test_factorial_num():
	assert fact(5) == 120

def test_squares_num():
	assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5:25}

def test_vowels_string():
	assert vowels("transferred") == 3
