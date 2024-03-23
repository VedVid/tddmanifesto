# -*- coding: utf-8 -*-


import pytest

from kata_5 import BarcodeScanner


def test__should_return_correct_price__when_12345_barcode_given():
    barcode_scanner = BarcodeScanner()

    result = barcode_scanner.scan("12345")

    assert result == "$7.25"


def test__should_return_correct_price__when_23456_barcode_given():
    barcode_scanner = BarcodeScanner()

    result = barcode_scanner.scan("23456")

    assert result == "$12.50"


def test__should_return_error__when_9999_barcode_given():
    barcode_scanner = BarcodeScanner()

    result = barcode_scanner.scan("9999")

    assert result == "Error: barcode not found"
