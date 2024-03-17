# -*- coding: utf-8 -*-


import pytest

from kata_1 import FizzBuzzSolver


def test__should_return_correct_fizzbuzz_string__when_numeric_argument_is_provided():
    # Arrange
    fizzbuzz_solver = FizzBuzzSolver()

    # Act
    fizzbuzz_string = fizzbuzz_solver.solve(15)

    # Assert
    assert (
        fizzbuzz_string
        == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz"
    )
