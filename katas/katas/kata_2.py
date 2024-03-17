# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(*args):
        str_values = []
        for arg in args:
            if arg == "":
                str_values.append("0")
                continue
            str_values.extend(arg.split(","))
        int_values = [int(x) for x in str_values]
        return sum(int_values)
