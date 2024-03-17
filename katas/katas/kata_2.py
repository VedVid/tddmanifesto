# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(exprstr, *args):
        if not args:
            if exprstr == "":
                return 0
            elif exprstr.isdigit() or (exprstr[1:].isdigit() and exprstr[0] == "-"):
                return int(exprstr)
            else:
                str_values = exprstr.split(",")
                int_values = [int(x) for x in str_values]
                return sum(int_values)
        str_values = exprstr.split(",")
        for arg in args:
            if arg == "":
                str_values.append("0")
                continue
            str_values.extend(arg.split(","))
        int_values = [int(x) for x in str_values]
        return sum(int_values)
