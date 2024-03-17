# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(*args):
        str_values = []
        for arg in args:
            if arg == "":
                str_values.append("0")
                continue
            if not arg[-1].isdigit():
                raise Exception(
                    "Separator at the end of string is not allowed"
                ) from ValueError
            if arg[:2] == "//":
                left = "//"
                right = "\n"
                sep = arg[arg.index(left) + len(left) : arg.index(right)]
                new_arg = arg[arg.index(right) + len(right) :]
                new_arg = new_arg.replace(sep, ",")
            else:
                new_arg = arg.replace("\n", ",")
            str_values.extend(new_arg.split(","))
        int_values = [int(x) for x in str_values]
        return sum(int_values)
