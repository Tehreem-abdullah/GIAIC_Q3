# MODULES & FUNCTIONS
# 1. Built-in modules
# 2. User-defined modules
# 3. Importing modules

# 1.1 Built-in modules
# Importing necessary built-in modules

import math            # For mathematical operations
import random          # For generating random numbers
import os              # For interacting with the operating system
import datetime        # For working with dates and times

# --- Math Module --- #
def math_operations():
    num = 16
    print("Square Root of", num, "is:", math.sqrt(num))  # Square root
    print("Factorial of", num, "is:", math.factorial(5))  # Factorial

# --- Random Module --- #
def random_example():
    random_number = random.randint(1, 100)  # Generate random number between 1 and 100
    print("Random number between 1 and 100:", random_number)

# --- OS Module --- #
def os_operations():
    current_directory = os.getcwd()  # Get current working directory
    print("Current Directory:", current_directory)
    print("List of files in the current directory:", os.listdir(current_directory))

# --- Datetime Module --- #
def datetime_example():
    current_time = datetime.datetime.now()  # Get current date and time
    print("Current Date and Time:", current_time)
    print("Year:", current_time.year)
    print("Month:", current_time.month)
    print("Day:", current_time.day)

# --- Main Function --- #
def main():
    print("==== Math Operations ====")
    math_operations()
    
    print("\n==== Random Number Example ====")
    random_example()
    
    print("\n==== OS Operations ====")
    os_operations()

    print("\n==== Date and Time Example ====")
    datetime_example()

if __name__ == "__main__":
    main()
# This code demonstrates the use of built-in modules in Python.

# 1.2 User-defined modules
## greetings.py

def say_hello(Tehreem):
    """Function to greet a person."""
    return f"Hello, {Tehreem}!"

def say_goodbye(Tehreem):
    """Function to bid farewell to a person."""
    return f"Goodbye, {Tehreem}!"

def ask_how_are_you(Tehreem):
    """Function to ask how a person is."""
    return f"How are you, {Tehreem}?"

# This is a simple user-defined module that contains functions to greet, bid farewell, and ask how someone is doing.

# 1.3 Importing modules
# Example using the built-in `math` module

import math

def calculate_square_root(num):
    return math.sqrt(num)

def calculate_factorial(num):
    return math.factorial(num)

# Test the functions
num = 16
print(f"Square root of {num}: {calculate_square_root(num)}")
print(f"Factorial of {num}: {calculate_factorial(5)}")

