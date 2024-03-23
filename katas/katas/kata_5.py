# -*- coding: utf-8 -*-


class BarcodeScanner:

    d = {
        "12345": "$7.25",
        "23456": "$12.50",
        "9999": "Error: barcode not found"
    }

    def scan(self, barcode):
        return self.d[barcode]
