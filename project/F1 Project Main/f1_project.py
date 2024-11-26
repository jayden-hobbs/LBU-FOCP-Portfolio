#!/usr/bin/env python3

class f1_driver:
    def __init__(self, name, team, nationality, driver_number, code):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.driver_number = driver_number
        self.code = code

def driver_details(file_path):
    drivers = []
    try:
        with open("f1_drivers.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    driver_number, name, team, nationality, code = data
                    driver = f1_driver(
                        driver_number = int(driver_number.strip()),
                        code = code.strip(),
                        name = name.strip(),
                        team = team.strip(),
                        nationality = nationality.strip()
                    )
                    drivers.append(driver)

    except FileNotFoundError:
        print("File not found")

    except ValueError:
        print("Invalid data in file")

    return drivers

if __name__ == "__main__":
    # Path to the input file
    input_file = "f1_project"  # Update with your text file path

    # Call the subfunction to create driver instances
    all_drivers = driver_details(input_file)

    # Display details of all driver instances
    print("All F1 Drivers:")
    for driver in all_drivers:
        driver.display_details()
        print("-" * 40)