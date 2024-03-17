# -*- coding: utf-8 -*-


import pytest

from kata_2 import Calculator


def test__should_return_zero__when_string_is_empty():
    # Arrange
    calc = Calculator()

    # Act
    result = Calculator.add("")

    # Assert
    assert result == 0
