# -*- coding: utf-8 -*-


import pytest

from kata_3 import Validator


def test__should_return_error__when_password_is_shorter_than_8_characters():
    validator = Validator()

    result_1 = validator.valide("")
    result_2 = validator.valide("1234567")

    assert result_1 == "Password must be at least 8 characters"
    assert result_2 == "Password must be at least 8 characters"
