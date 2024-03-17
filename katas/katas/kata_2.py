# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(exprstr):
        if exprstr == "":
            return 0
        elif exprstr.isdigit() or (exprstr[1:].isdigit() and exprstr[0] == "-"):
            return int(exprstr)
