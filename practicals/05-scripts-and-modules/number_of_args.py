# # #1/usr/bin/env python3

# # import sys

# # number = 5+5

# # def arguments(number):
# #     print (number)
    

# # if __name__ == '__main__':
# #     arguments(number)
# #     number_of_args = len(sys.argv) - 1
# #     print(f'Number of arguments: {number_of_args}')

# import sys

# def process_arguments(arg1, arg2, arg3, arg4, arg5):
#     # Highlighting each argument by printing them
#     print(f"Argument 1: {arg1}")
#     print(f"Argument 2: {arg2}")
#     print(f"Argument 3: {arg3}")
#     print(f"Argument 4: {arg4}")
#     print(f"Argument 5: {arg5}")

# if __name__ == "__main__":
#     # Ensure exactly 5 arguments are passed (including the script name itself)
#     if len(sys.argv) != 6:
#         print("Error: Please provide exactly 5 arguments.")
#         sys.exit(1)

#     # Capture the arguments
#     argument1 = sys.argv[1]
#     argument2 = sys.argv[2]
#     argument3 = sys.argv[3]
#     argument4 = sys.argv[4]
#     argument5 = sys.argv[5]

#     # Call the function to process and highlight the arguments
#     process_arguments(argument1, argument2, argument3, argument4, argument5)
import sys

def display_arguments(arg1, arg2, arg3):
    # Highlighting and printing each argument passed to the function
    print(f"Argument 1: {arg1}")  # Argument 1 will be passed as the first command-line argument
    print(f"Argument 2: {arg2}")  # Argument 2 will be passed as the second command-line argument
    print(f"Argument 3: {arg3}")  # Argument 3 will be passed as the third command-line argument

if __name__ == "__main__":
    # Check if we received exactly 4 command-line arguments (script name + 3 arguments)
    if len(sys.argv) != 4:
        print("Error: Please provide exactly 3 arguments.")
        sys.exit(1)

    # Capturing the arguments from sys.argv (index 1 to 3)
    argument1 = sys.argv[1]  # This is the first argument you pass when running the script
    argument2 = sys.argv[2]  # This is the second argument you pass when running the script
    argument3 = sys.argv[3]  # This is the third argument you pass when running the script

    # Call the function to display the arguments
    display_arguments(argument1, argument2, argument3)
