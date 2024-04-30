import pytest
from password_validator import *

def test_password_strength():
	result = Validator.test_password_strength("Test123!")
	assert result[2] == "Very Strong"

def test_password_validity_value():
	result = Validator.test_password_strength("Test123")
	assert result[1] == 3
	
def test_password_validity_error():
	result = Validator.test_password_strength("test123!")
	assert result[0] == "Password should contain at least one uppercase letter."

def test_password_validity_error():
	result = Validator.test_password_strength("TEST123!")
	assert result[0] == "Password should contain at least one lowercase letter."

def test_password_validity_error():
	result = Validator.test_password_strength("123456")
	assert result[0] == "Password is most common password list."