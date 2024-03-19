# -*- coding: utf-8 -*-


class Validator:
    @staticmethod
    def valide(password):
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if sum(ch.isdigit() for ch in password) < 2:
            errors.append("The password must contain at least 2 numbers")
        return errors
