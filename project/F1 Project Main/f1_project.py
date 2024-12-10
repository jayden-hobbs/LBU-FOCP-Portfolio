#!/usr/bin/env python3

import argparse

class f1_driver:
    all_drivers = []

    def __init__(self, driver_number, code, name, team, nationality):
        self.number = driver_number
        self.code = code
        self.name = name
        self.team = team
        self.nationality = nationality
        
        f1_driver.all_drivers.append(self)


def create_drivers(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.split(',')

                if len(data) == 5:
                    try:
                       driver_number, code, name, team, nationality = [item.strip() for item in data]
                       driver = f1_driver(driver_number, code, name, team, nationality)
                    except ValueError:
                        print("Invalid data in file")
                else:
                    print("Invalid data in file. Please check the file and try again.")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_drivers():
    for driver in f1_driver.all_drivers:
        print(f"Driver {driver.name} with number {driver.number} is from {driver.nationality} and drives for {driver.team}")

def main():
    parser = argparse.ArgumentParser(description="F1 Driver Management System")
    parser.add_argument("file_path", help="Path to the file containing driver data")
    args = parser.parse_args()

    create_drivers(args.file_path)
    print_drivers()

if __name__ == "__main__":
    main() 
                                                                                           



