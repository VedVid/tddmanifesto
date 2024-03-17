# -*- coding: utf-8 -*-


from katas import kata_1, kata_2


if __name__ == "__main__":
    fizz_buzz_solver = kata_1.FizzBuzzSolver()
    print("Kata 1:")
    print("Fizz Buzz of 35")
    print(fizz_buzz_solver.solve(35))
    print()
    string_calculator = kata_2.Calculator()
    print("Kata 2:")
    print('Result of "//sep\ n2sep5"')
    print(string_calculator.add("//sep\n2sep5"))
