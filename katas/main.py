# -*- coding: utf-8 -*-


from katas import kata_1, kata_2, kata_3, kata_4, kata_5


if __name__ == "__main__":
    fizz_buzz_solver = kata_1.FizzBuzzSolver()
    print("Kata 1:")
    print("Fizz Buzz of 35")
    print(fizz_buzz_solver.solve(35))
    print()
    string_calculator = kata_2.Calculator()
    print("Kata 2:")
    print(r'Result of "//sep\n2sep5"')
    print(string_calculator.add("//sep\n2sep5"))
    print()
    password_validator = kata_3.Validator()
    print("Kata 3:")
    print('Validate password "password":')
    print(password_validator.valide("password"))
    print()
    city_finder = kata_4.CityFinder()
    print("Kata 4:")
    print('Search for cities with "ri":')
    print(city_finder.find("ri"))
    print()
    barcode_scanner = kata_5.BarcodeScanner()
    print("Kata 5:")
    print('Result of barcode "12345":')
    print(barcode_scanner.scan("12345"))
    print()
