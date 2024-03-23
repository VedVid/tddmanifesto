# -*- coding: utf-8 -*-


import pytest

from kata_5 import BarcodeScanner


def test__should_return_correct_price__when_12345_barcode_given():
    barcode_scanner = BarcodeScanner()

    result = barcode_scanner.scan("12345")

    assert result == "$7.25"
