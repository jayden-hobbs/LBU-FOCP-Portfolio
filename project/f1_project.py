#!/usr/bin/env python3

import argparse
from tabulate import tabulate
import sys
from collections import defaultdict
import os

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
            if driver.code.strip() == code.strip():
                return driver
        return None

    @classmethod
    def get_team_by_team(cls, team):
        for driver in cls.all_drivers:
            if driver.team.strip() == team.strip():
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
    headers=["NUMBER", "CODE", "NAME", "TEAM", "NATIONALITY"]
    print(tabulate(drivers, headers=headers, tablefmt="fancy_grid"))

def fastest_lap_of_race(filename):
    fastest_driver = None
    fastest_time = float('inf')

    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                driver_code = line[:3].strip()
                lap_time_str = line[3:].strip()

                try:
                    lap_time = float(lap_time_str)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

                if lap_time < fastest_time:
                    fastest_time = lap_time
                    fastest_driver = driver_code

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        return

    if fastest_driver:
        driver_details = f1_driver.get_driver_by_code(fastest_driver)
        if driver_details:
            driver_data = [
                ["DRIVER", "CODE", "NUMBER", "TEAM", "NATIONALITY", "TIME"],
                [driver_details.name, driver_details.code, driver_details.number, driver_details.team, driver_details.nationality, fastest_time]
            ]
            print(tabulate(driver_data, headers="firstrow", tablefmt="grid"))
        else:
            print(f"No driver found for the fastest lap: {fastest_driver}")
    else:
        print("No valid lap times found.")

def average_times(filename):
    with open(filename, 'r') as file:
        next(file)
        lap_times = [float(line[3:].strip()) for line in file]
        average_time = round(sum(lap_times) / len(lap_times), 3)
        print(f"{average_time} seconds")

def lap_standings(filename):
    lap_times = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            driver = str(line[:3])
            lap_time = float(line[3:].strip())
            lap_times.append((driver, lap_time))

    lap_times.sort(key=lambda x: x[1])
    table_data = [(index + 1, driver, time) for index, (driver, time) in enumerate(lap_times)]
    headers = ["POSITION", "DRIVER", "TIME"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def drivers_fastest_lap(filename):
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

    table_data.sort(key=lambda x: x[4])

    headers = ["NAME", "CODE", "NATIONALITY", "TEAM", "FASTEST LAP TIME (S)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def drivers_average_time(filename):
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

    table_data.sort(key=lambda x: x[4])   
    
    headers = ["NAME", "CODE", "NATIONALITY", "TEAM", "AVERAGE LAP TIME (S)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def driver_lap_times(filename):
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
            driver = str(line[:3]).strip()
            lap_time = float(line[3:].strip())
            if driver == driverChoice:
                lap_data.append((driver, lap_number, lap_time))
                lap_number += 1

    if lap_data:
        headers = ["DRIVER", "LAP NUMBER", "LAP TIME"]
        print(tabulate(lap_data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Driver has no lap times for the selected race.")

def get_team_times(filename):
    teams = ["Red Bull Racing", "Mercedes", "Ferrari", "McLaren", "Aston Martin", "Alpine", "RB", "Kick Sauber", "Haas", "Williams"]
    for index, team in enumerate(teams, 1):
        print(f"{index}. {team}")
    
    try:
        team = teams[int(input("Select the team number: ")) - 1]
        team_lap_times = []

        drivers_in_team = {driver.code: driver for driver in f1_driver.all_drivers if driver.team.strip() == team.strip()}

        if not drivers_in_team:
            print(f"No drivers found for {team}")
            return

        driver_lap_counts = {driver.code: 0 for driver in drivers_in_team.values()}

        with open(filename, 'r') as file:
            next(file)
            for line in file:
                driver_code, lap_time_str = line[:3].strip(), line[3:].strip()
                try:
                    lap_time = float(lap_time_str)
                except ValueError:
                    continue

                if driver_code in drivers_in_team:
                    driver = drivers_in_team[driver_code]
                    driver_lap_counts[driver_code] += 1
                    lap_number = driver_lap_counts[driver_code]
                    team_lap_times.append((driver.name, driver.code, driver.team, lap_number, lap_time))

        if team_lap_times:
            print(tabulate(team_lap_times, headers=["NAME", "CODE", "TEAM", "DRIVER LAP NUMBER", "LAP TIME (S)"], tablefmt="fancy_grid"))
        else:
            print(f"No lap times found for {team}")
    
    except (ValueError, IndexError):
        print("Invalid input! Please select a valid team number.")

def get_file():
    files = os.listdir()
    excluded_files = ["f1_drivers.txt", "requirements.txt"]
    txt_files = [file for file in files if file.endswith(".txt") and file not in excluded_files]
    
    if not txt_files:
        print("No valid .txt files found in the current directory.")
        sys.exit()

    print("The following files are available:")
    for index, file in enumerate(txt_files, 1):
        print(f"{index}. {file}")

    while True:
        try:
            choice = int(input("Please select the file you would like to use: "))
            if 1 <= choice <= len(txt_files):  
                filename = txt_files[choice - 1]
                print(f"You selected: {filename}")

                try:
                    with open(filename, 'r') as file:
                        lines = file.readlines()

                        lines_with_data = sum(1 for line in lines if line.strip() != '')

                        if lines_with_data <= 1:
                            print(f"The file {filename} is empty or contains no lap times.")
                            
                        else:
                            return filename
                            break
                        
                except Exception as e:
                    print(f"Error reading the file: {e}")
                    return None
            else:
                print("Invalid choice. Please select a valid file number.")
                continue
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="F1 Driver Management System")
    parser.add_argument("file_path", help="Path to the file containing driver data")
    args = parser.parse_args()

    create_drivers(args.file_path)
    
    print("Welcome to the F1 Driver Management System")
    
    filename = get_file()

    while True:
        print("Please select an option:")
        print("1. View all drivers")
        print("2. View the fastest lap of the file")
        print("3. View the average lap time for the file")
        print("4. View the lap standings for the file")
        print("5. View the fastest lap for each driver in the file")
        print("6. View the average lap time for each driver in the file")
        print("7. View lap times for a specific driver")
        print("8. View all laps for a specific team")
        print("9. Change the race data file")
        print("x. Exit")
        
        try:
            choice = input("Enter your choice ~ ")
            
            if choice == "1":
                print_drivers()
            elif choice == "2":
                fastest_lap_of_race(filename)
            elif choice == "3":
                average_times(filename)
            elif choice == "4":
                lap_standings(filename)
            elif choice == "5":
                drivers_fastest_lap(filename)
            elif choice == "6":
                drivers_average_time(filename)
            elif choice == "7":
                driver_lap_times(filename)
            elif choice == "8":
                get_team_times(filename)
            elif choice == "9":
                filename = get_file()
                if filename is None:
                    print("No valid files available to select.")
                    continue
            elif choice == "x":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please select a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
