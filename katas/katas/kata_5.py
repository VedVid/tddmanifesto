# -*- coding: utf-8 -*-


class BarcodeScanner:

    d = {
        "12345": "$7.25"
    }

    def scan(self, barcode):
        return self.d[barcode]
