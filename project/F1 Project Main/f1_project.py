#!/usr/bin/env python3

class f1_driver:
    all_drivers = []  # This will hold all the driver instances

    def __init__(self, name, team, nationality, driver_number, code):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.driver_number = driver_number
        self.code = code
        
        # Add this instance to the class-level all_drivers list
        f1_driver.all_drivers.append(self)

    @classmethod
    def print_all_drivers(cls):
        """Class method to print all driver instances."""
        if not cls.all_drivers:
            print("No drivers found!")
        else:
            for driver in cls.all_drivers:
                print(f"{driver.driver_number} {driver.name} {driver.team}")


def driver_details(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(f"Reading line: {line.strip()}")  # Debugging: See what line is being read
                data = line.strip().split(",")
                print(f"Data split: {data}")  # Debugging: Show the split data to see what it looks like
                
                if len(data) == 5:  # We expect 5 values per line
                    try:
                        driver_number, code, name, team, nationality = [item.strip() for item in data]  # Strip spaces
                        driver = f1_driver(
                            driver_number = int(driver_number),  # Ensure driver_number is an integer
                            code = code,
                            name = name,
                            team = team,
                            nationality = nationality
                        )
                        print(f"Created driver: {name}")  # Debugging: See which driver is being created
                    except ValueError as ve:
                        print(f"Error processing line: {line.strip()}")  # Debugging: Print the line with error
                        print(f"ValueError: {ve}")
                else:
                    print(f"Invalid line format: {line.strip()}")  # Debugging: Print lines that don't match expected format

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
drivers = driver_details(r"C:\Users\Seagu\OneDrive - Leeds Beckett University\Computer Programming\Visual Studio Code\programming-portfolio-jayden-hobbs\project\F1 Project Main\f1_drivers.txt")  # Provide the correct file path

# Print all drivers using the class method
f1_driver.print_all_drivers()
