# -*- coding: utf-8 -*-


from collections import defaultdict


class BarcodeScanner:

    d = defaultdict(lambda: "Error: barcode not found")
    d["12345"] = "$7.25"
    d["23456"] = "$12.50"

    def scan(self, barcode):
        if barcode:
            return self.d[barcode]
        return "Error: empty barcode"

    def total(self, *args):
        total_price = 0
        for arg in args:
            sprice = self.scan(arg)
            fprice = float(sprice[1:])
            total_price += fprice
        return "$" + str(total_price)
