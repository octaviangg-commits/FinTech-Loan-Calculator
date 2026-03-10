import pytest
from app import calculate_loan

def test_calculate_loan():
    assert calculate_loan(10000, 5, 5) == 188.71  # Expected monthly payment for given values
    assert calculate_loan(20000, 7, 10) == 232.22
    assert calculate_loan(5000, 0, 5) == 83.33  # Zero interest scenario
