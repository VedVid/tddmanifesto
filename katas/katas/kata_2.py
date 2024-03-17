# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(exprstr):
        if exprstr == "":
            return 0
        elif exprstr.isdigit() or (exprstr[1:].isdigit() and exprstr[0] == "-"):
            return int(exprstr)
        else:
            str_values = exprstr.split(",")
            int_values = [int(x) for x in str_values]
            return sum(int_values)
