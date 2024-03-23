# -*- coding: utf-8 -*-


import pytest

from kata_4 import CityFinder


def test__should_return_none__when_search_text_is_shorter_than_2_character():
    city_finder = CityFinder()

    result = city_finder.find("a")

    assert result is None


def test__should_return_something__when_seaerch_text_is_longer_or_equal_to_two_characters():
    city_finder = CityFinder()

    result = city_finder.find("aa")

    assert result is not None
