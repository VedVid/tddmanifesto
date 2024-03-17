# -*- coding: utf-8 -*-


import pytest

from kata_2 import Calculator


def test__should_return_zero__when_string_is_empty():
    # Arrange
    calc = Calculator()

    # Act
    result = calc.add("")

    # Assert
    assert result == 0


def test__should_return_number__when_string_has_only_one_number():
    calc = Calculator()

    result_1 = calc.add("1")
    result_2 = calc.add("54")

    assert result_1 == 1
    assert result_2 == 54
