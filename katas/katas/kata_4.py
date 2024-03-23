# -*- coding: utf-8 -*-


class CityFinder:
    cities = [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", "Amsterdam", "Vienna", "Sydney",
        "New York City", "London", "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]

    def find(self, searchtxt):
        if len(searchtxt) < 2:
            return None
        else:
            cities_found = []
            for city in self.cities:
                if searchtxt in city:
                    cities_found.append(city)
            if not cities_found:
                return None
            return cities_found
