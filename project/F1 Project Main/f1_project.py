#!/usr/bin/env python3

class f1_driver:
    all_drivers = []

    def __init__(self, name, team, nationality, driver_number, code):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.driver_number = driver_number
        self.code = code
        
        f1_driver.all_drivers.append(self)

