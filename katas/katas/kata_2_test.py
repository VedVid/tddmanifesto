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


def test__should_return_number__when_string_has_only_one_positive_number():
    calc = Calculator()

    result_1 = calc.add("1")
    result_2 = calc.add("54")

    assert result_1 == 1
    assert result_2 == 54


def test__should_return_number__when_string_has_only_one_negative_number():
    calc = Calculator()

    result_1 = calc.add("-4")
    result_2 = calc.add("-33")

    assert result_1 == -4
    assert result_2 == -33


def test__should_return_sum_of_numbers__when_string_contains_two_numbers_separated_with_comma():
    calc = Calculator()

    result_1 = calc.add("1,2")
    result_2 = calc.add("12,-13")

    assert result_1 == 3
    assert result_2 == -1


def test__should_return_sum_of_numbers__when_string_contains_many_numbers_separated_with_commas():
    calc = Calculator()

    result_1 = calc.add("1,2,3")
    result_2 = calc.add("15,75,-24")
    result_3 = calc.add("-3,-2,-1,0,1,2,3")

    assert result_1 == 6
    assert result_2 == 66
    assert result_3 == 0


def test__should_return_sum_of_all_numbers_in_all_arguments__when_multiple_arguments_passed():
    calc = Calculator()

    result_1 = calc.add("1", "2")
    result_2 = calc.add("-5,2", "8,24", "")

    assert result_1 == 3
    assert result_2 == 29


def test__should_return_sum_of_all_numbers__when_there_is_newline_instead_of_comma():
    calc = Calculator()

    result = calc.add("1,2\n3")

    assert result == 6


def test__should_raise_exception__when_string_ends_with_separator_comma():
    calc = Calculator()

    with pytest.raises(Exception):
        calc.add("1,2,")


def test__should_raise_exception__when_string_ends_with_separator_newline():
    calc = Calculator()

    with pytest.raises(Exception):
        calc.add("1,2\n")


def test__should_handle_custom_delimiters__when_specific_string_format_is_passed():
    calc = Calculator()

    result_1 = calc.add("//;\n1;3")
    result_2 = calc.add("//|\n1|2|3")
    result_3 = calc.add("//sep\n2sep5")

    assert result_1 == 4
    assert result_2 == 6
    assert result_3 == 7


def test__should_raise_exception__when_string_does_not_have_consistent_separators():
    calc = Calculator()

    with pytest.raises(Exception, match="separator expected but"):
        calc.add("//|\n1|2,3")
