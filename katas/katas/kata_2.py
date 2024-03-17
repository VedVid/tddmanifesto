# -*- coding: utf-8 -*-


class Calculator:
    @staticmethod
    def add(exprstr):
        if exprstr == "":
            return 0
        elif exprstr.isdigit():
            return int(exprstr)
        elif exprstr[1:].isdigit():
            return int(exprstr)