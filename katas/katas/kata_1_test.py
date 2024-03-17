# -*- coding: utf-8 -*-


import pytest


def test__should_return_number__when_user_start_function():
    # Arrange
    fizzbuzz_solver = FizzBuzzSolver()

    # Act
    fizzbuzz_string = fizzbuzz_solver.solve(15)

    assert fizzbuzz_string == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz"
