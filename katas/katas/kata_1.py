# -*- coding: utf-8 -*-


class FizzBuzzSolver:
    @staticmethod
    def solve(number):
        values = []
        for i in range(1, number+1):
            if i % 3 == 0 and i % 5 == 0:
                values.append("Fizz Buzz")
            elif i % 3 == 0:
                values.append("Fizz")
            elif i % 5 == 0:
                values.append("Buzz")
            else:
                values.append(str(i))
        return ", ".join(values)
