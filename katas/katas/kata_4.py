# -*- coding: utf-8 -*-


class CityFinder:
    cities = [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", "Amsterdam", "Vienna", "Sydney",
        "New York City", "London", "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]

    def find(self, searchtxt):
        if len(searchtxt) < 2:
            return None
