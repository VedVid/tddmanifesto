# -*- coding: utf-8 -*-


import pytest


def test__should_return_zero__when_string_is_empty():
    # Arrange
    calc = Calculator()

    # Act
    result = Calculator.add("")

    # Assert
    assert result == ""
