#!/usr/bin/env python3

import argparse
from tabulate import tabulate
import sys
from collections import defaultdict

class f1_driver:
    all_drivers = []

    def __init__(self, driver_number, code, name, team, nationality):
        self.number = driver_number
        self.code = code
        self.name = name
        self.team = team
        self.nationality = nationality
        
        f1_driver.all_drivers.append(self)

    @classmethod
    def get_driver_by_code(cls, code):
        for driver in cls.all_drivers:
            if driver.code == code:
                return driver
        return None

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
                        sys.exit()
                else:
                    print("Invalid data in file. Please check the file and try again.")
                    sys.exit()

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")

def print_drivers():
    drivers = []
    for driver in f1_driver.all_drivers:
        if driver:
            drivers.append([driver.number, driver.code, driver.name, driver.team, driver.nationality])
        else:
            print("No drivers found")
    headers=["Number", "Code", "Name", "Team", "Nationality"]
    print(tabulate(drivers, headers=headers, tablefmt="fancy_grid"))

from tabulate import tabulate

class f1_driver:
    all_drivers = []

    def __init__(self, driver_number, code, name, team, nationality):
        self.number = driver_number
        self.code = code
        self.name = name
        self.team = team
        self.nationality = nationality
        f1_driver.all_drivers.append(self)

def fastest_lap_of_race():
    while True:
        try:
            choice = int(input("Please select which race you would like to view the fastest lap for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) ~ "))
            
            if choice == 1:
                filename = "lap_times_1.txt"
                print("Dewsbury Race 1 Fastest Lap is...  \n")
                break
            elif choice == 2:
                filename = "lap_times_2.txt"
                print("Dewsbury Race 2 Fastest Lap is... \n")
                break
            elif choice == 3:
                filename = "lap_times_3.txt"
                print("York Fastest Lap is... \n")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")
            continue

    fastest_driver = None
    fastest_time = float('inf')

    with open(filename, 'r') as file:
        next(file)
        for line in file:
            driver_code = str(line[:3].strip())
            lap_time = float(line[3:].strip())
            
            if lap_time < fastest_time:
                fastest_time = lap_time
                fastest_driver = driver_code

    driver_details = None
    for driver in f1_driver.all_drivers:
        if driver.code == fastest_driver:
            driver_details = driver
            break

    if driver_details:
        driver_data = [
            ["Driver", "Code", "Number", "Team", "Nationality"],
            [driver_details.name, driver_details.code, driver_details.number, driver_details.team, driver_details.nationality]
        ]
        
        print(tabulate(driver_data, headers="firstrow", tablefmt="grid"))
    else:
        print("No driver found for the fastest lap.")


def average_times():
    while True:
        try:
            choice = int(input("Please select which race you would like to view the average lap time for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) "))
            
            if choice == 1:
                filename = "lap_times_1.txt"
                print("Dewsbury Race 1 Average Lap Time is...")
                break
            elif choice == 2:
                filename = "lap_times_2.txt"
                print("Dewsbury Race 2 Average Lap Time is...")
                break
            elif choice == 3:
                filename = "lap_times_3.txt"
                print("York Average Lap Time is...")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")

    with open(filename, 'r') as file:
        next(file)
        lap_times = [float(line[3:].strip()) for line in file]
        average_time = round(sum(lap_times) / len(lap_times), 3)
        print(f"{average_time} seconds")


def lap_standings():
    while True:
        try:
            choice = int(input("Please select which race you would like to view the lap standings for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) ~ "))
            
            if choice == 1:
                filename = "lap_times_1.txt"
                print("Dewsbury Race 1 Lap Standings:")
                break
            elif choice == 2:
                filename = "lap_times_2.txt"
                print("Dewsbury Race 2 Lap Standings:")
                break
            elif choice == 3:
                filename = "lap_times_3.txt"
                print("York Lap Standings:")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")

    lap_times = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            driver = str(line[:3])
            lap_time = float(line[3:].strip())
            lap_times.append((driver, lap_time))

    lap_times.sort(key=lambda x: x[1])
    table_data = [(index + 1, driver, time) for index, (driver, time) in enumerate(lap_times)]
    headers = ["Position", "Driver", "Time"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def drivers_fastest_lap():
    while True:
        try:
            choice = int(input("Please select which race you would like to view each driver's fastest lap for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) ~ "))
            
            if choice == 1:
                filename = "lap_times_1.txt"
                print("The fastest lap for each driver in Dewsbury Race 1 is...")
                break
            elif choice == 2:
                filename = "lap_times_2.txt"
                print("The fastest lap for each driver in Dewsbury Race 2 is...")
                break
            elif choice == 3:
                filename = "lap_times_3.txt"
                print("The fastest lap for each driver in York is...")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")

    fastest_laps = defaultdict(lambda: float('inf'))
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            driver = str(line[:3])
            lap_time = float(line[3:].strip())
            
            if lap_time < fastest_laps[driver]:
                fastest_laps[driver] = lap_time
    
    table_data = []
    for driver_code, lap_time in fastest_laps.items():
        driver = f1_driver.get_driver_by_code(driver_code)
        if driver:
            table_data.append((driver.name, driver.code, driver.nationality, driver.team, lap_time))
        else:
            print(f"Driver with code {driver_code} not found")

    headers = ["Name", "Code", "Nationality", "Team", "Fastest Lap Time (s)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def drivers_average_time():
    while True:
        try:
            choice = int(input("Please select which race you would like to view each driver's average lap time for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) ~ "))
            
            if choice == 1:
                filename = "lap_times_1.txt"
                print("The average lap time for each driver in Dewsbury Race 1 is...")
                break
            elif choice == 2:
                filename = "lap_times_2.txt"
                print("The average lap time for each driver in Dewsbury Race 2 is...")
                break
            elif choice == 3:
                filename = "lap_times_3.txt"
                print("The average lap time for each driver in York is...")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")

    lap_times = defaultdict(lambda: {'total_time': 0, 'num_laps': 0})
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            driver = str(line[:3])
            lap_time = float(line[3:].strip())
            lap_times[driver]['total_time'] += lap_time
            lap_times[driver]['num_laps'] += 1

    table_data = []
    for driver_code, data in lap_times.items():
        average_time = data['total_time'] / data['num_laps']
        driver = f1_driver.get_driver_by_code(driver_code)
        if driver:
            table_data.append((driver.name, driver.code, driver.nationality, driver.team, average_time))   
        else:
            print(f"Driver with code {driver_code} not found")
    
    headers = ["Name", "Code", "Nationality", "Team", "Average Lap Time (s)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def driver_lap_times():
    while True:
        try:
            raceChoice = int(input("Please select which race you would like to view drivers lap times for: Dewsbury Race 1 (1), Dewsbury Race 2 (2) or York (3) ~ "))
            if raceChoice == 1:
                filename = "lap_times_1.txt"
                print("The fastest lap for each driver in Dewsbury Race 1 is...")
                break
            elif raceChoice == 2:
                filename = "lap_times_2.txt"
                print("The fastest lap for each driver in Dewsbury Race 2 is...")
                break
            elif raceChoice == 3:
                filename = "lap_times_3.txt"
                print("The fastest lap for each driver in York is...")
                break
            else:
                print("Invalid choice. Please select either 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number (1, 2, or 3).")
    
    while True:
        try:
            driverChoice = input("Please enter the driver code you would like to view lap times for: ")
            driver = f1_driver.get_driver_by_code(driverChoice)
            if driver:
                break
            else:
                print("Driver not found. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid driver code.")
    
    lap_data = []
    with open(filename, 'r') as file:
        next(file)
        lap_number = 1
        for line in file:
            driver = str(line[:3])
            lap_time = float(line[3:].strip())
            if driver == driverChoice:
                lap_data.append((lap_number, lap_time))
                lap_number += 1

    if lap_data:
        headers = ["Lap Number", "Lap Time"]
        print(tabulate(lap_data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Driver has no lap times for selected race")
    
       
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="F1 Driver Management System")
    parser.add_argument("file_path", help="Path to the file containing driver data")
    args = parser.parse_args()

    create_drivers(args.file_path)
    print("Welcome to the F1 Driver Management System")
    while True:
        print("Please select an option:")
        print("1. View all drivers")
        print("2. View the fastest lap of each race")
        print("3. View the average lap time for each race")
        print("4. View the lap standings for each race")
        print("5. View the fastest lap for each driver in each race")
        print("6. View the average lap time for each driver in each race")
        print("7. View lap times for a specific driver")
        print("8. Exit")
        
        try:
            choice = int(input("Enter your choice ~ "))
            
            if choice == 1:
                print_drivers()
            elif choice == 2:
                fastest_lap_of_race()
            elif choice == 3:
                average_times()
            elif choice == 4:
                lap_standings()
            elif choice == 5:
                drivers_fastest_lap()
            elif choice == 6:
                drivers_average_time()
            elif choice == 7:
                driver_lap_times()
            elif choice == 8:
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")