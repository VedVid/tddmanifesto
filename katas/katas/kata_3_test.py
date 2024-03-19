# -*- coding: utf-8 -*-


import pytest

from kata_3 import Validator


def test__should_return_error__when_password_is_shorter_than_8_characters():
    validator = Validator()

    result_1 = validator.valide("")
    result_2 = validator.valide("1234567")
    result_3 = validator.valide("你好你好你好")

    assert result_1 == "Password must be at least 8 characters"
    assert result_2 == "Password must be at least 8 characters"
    assert result_3 == "Password must be at least 8 characters"


def test__should_return_error__when_password_lacks_two_numbers():
    validator = Validator()

    result = validator.valide("abcdefgh")

    assert result == "The password must contain at least 2 numbers"


def test__should_gather_all_errors__when_multiple_errors_encountered():
    validator = Validator()

    result = validator.valide("abcd")

    assert (
        "Password must be at least 8 characters" in result
        and "The password must contain at least 2 numbers" in result
    )
