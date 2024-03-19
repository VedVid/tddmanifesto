# -*- coding: utf-8 -*-


class Validator:
    @staticmethod
    def valide(password):
        if len(password) < 8:
            return "Password must be at least 8 characters"
