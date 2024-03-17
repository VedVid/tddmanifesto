# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(*args):
        str_values = []
        for arg in args:
            if arg == "":
                str_values.append("0")
                continue
            new_arg = arg.replace("\n", ",")
            str_values.extend(new_arg.split(","))
        int_values = [int(x) for x in str_values]
        return sum(int_values)
