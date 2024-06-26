# -*- coding: utf-8 -*-


import pytest

from kata_3 import Validator


def test__should_return_error__when_password_is_shorter_than_8_characters():
    validator = Validator()

    result_1 = validator.valide("")
    result_2 = validator.valide("1234567")
    result_3 = validator.valide("你好你好你好")
    result_4 = validator.valide("12345678")
    result_5 = validator.valide("你好你好你好你好")

    assert "Password must be at least 8 characters" in result_1
    assert "Password must be at least 8 characters" in result_2
    assert "Password must be at least 8 characters" in result_3
    assert "Password must be at least 8 characters" not in result_4
    assert "Password must be at least 8 characters" not in result_5


def test__should_return_error__when_password_lacks_two_numbers():
    validator = Validator()

    result_1 = validator.valide("abcdefgh")
    result_2 = validator.valide("12asdgfhrel")

    assert "The password must contain at least 2 numbers" in result_1
    assert "The password must contain at least 2 numbers" not in result_2


def test__should_gather_all_errors__when_multiple_errors_encountered():
    validator = Validator()

    result = validator.valide("abcd")

    assert (
        "Password must be at least 8 characters" in result
        and "The password must contain at least 2 numbers" in result
    )


def test__should_return_error__when_no_capital_letter_in_password():
    validator = Validator()

    result_1 = validator.valide("12345")
    result_2 = validator.valide("abcdef")
    result_3 = validator.valide("Abv132")

    assert "The password must contain at least one capital letter" in result_1
    assert "The password must contain at least one capital letter" in result_2
    assert "The password must contain at least one capital letter" not in result_3


def test__should_return_error__when_no_special_character_in_password():
    validator = Validator()

    result_1 = validator.valide("12345abcdef你好你")
    result_2 = validator.valide("12345abcdef%")

    assert "The password must contain at least one special character" in result_1
    assert "The password must contain at least one special character" not in result_2
