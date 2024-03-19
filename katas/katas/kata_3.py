# -*- coding: utf-8 -*-


class Validator:
    @staticmethod
    def valide(password):
        if len(password) < 8:
            return "Password must be at least 8 characters"
        if sum(ch.isdigit() for ch in password) < 2:
            return "The password must contain at least 2 numbers"
