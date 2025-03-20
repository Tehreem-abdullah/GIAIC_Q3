# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Function to calculate factorial using a loop
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return f"Factorial of {n} is {fact}"

# Function to print numbers from 1 to n using a loop
def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  # New line for better output formatting

# Main function
def main():
    num = int(input("Enter a number: "))

    # Using functions
    print(check_even_odd(num))
    print(factorial(num))

    print("\nPrinting numbers up to:", num)
    print_numbers(num)

# Execute main function
if __name__ == "__main__":
    main()


#Exception and Handling

# Function to check if a number is even or odd with exception handling
def check_even_odd(number):
    try:
        if number % 2 == 0:
            return f"{number} is Even"
        else:
            return f"{number} is Odd"
    except Exception as e:
        return f"Error: {e}"

# Function to calculate factorial with exception handling
def factorial(n):
    try:
        if n < 0:
            return "Factorial is not defined for negative numbers."
        
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return f"Factorial of {n} is {fact}"
    except Exception as e:
        return f"Error: {e}"

# Function to perform division and handle ZeroDivisionError
def divide_numbers(a, b):
    try:
        result = a / b
        return f"Result of {a} / {b} is {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Unexpected Error: {e}"

# Main function with input validation and exception handling
def main():
    try:
        num = int(input("Enter a number: "))
        print(check_even_odd(num))
        print(factorial(num))

        # Handling division operation with exception handling
        num1 = int(input("\nEnter first number for division: "))
        num2 = int(input("Enter second number for division: "))
        print(divide_numbers(num1, num2))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Execute main function
if __name__ == "__main__":
    main()

#File Handling

# Function to write data to a file 
def write_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
            return "Data written to file successfully."
    except Exception as e:
        return f"Error: {e}"
    
    # Function read data from a file
    def read_from_file(filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except Exception as e :
            return f"Error: {e}"
        
        #main function
        def main():
            filename = "data.txt"
            data = "Hello, Python!"

            # Write data to file
            print(write_to_file(filename, data))

            # Read data from file
            print(read_from_file(filename))


# Execute main function
if __name__ == "__main__":
    main()

#The math and data time calender

import math
import datetime
import calendar

# Function to perform basic math operations
def math_operations():
    try:
        num = float(input("Enter a number for math operations: "))
        print(f"Square root of {num}: {math.sqrt(num)}")
        print(f"{num} raised to power 3: {math.pow(num, 3)}")
        print(f"Factorial of {int(num)}: {math.factorial(int(num))}")
        print(f"Logarithm (base 10) of {num}: {math.log10(num)}")
        print(f"Sine of {num} radians: {math.sin(num)}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive number.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to display current date and time
def date_time_operations():
    now = datetime.datetime.now()
    print("\nCurrent Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Calculate difference between two dates
    try:
        year = int(input("Enter a year (YYYY): "))
        month = int(input("Enter a month (1-12): "))
        day = int(input("Enter a day (1-31): "))
        user_date = datetime.datetime(year, month, day)
        difference = now - user_date
        print(f"Days difference from today: {difference.days} days")
    except ValueError:
        print("Error: Invalid date input.")

# Function to display calendar
def calendar_operations():
    try:
        year = int(input("\nEnter a year for the calendar: "))
        month = int(input("Enter a month (1-12): "))
        print("\nCalendar for the month:")
        print(calendar.month(year, month))

        # Check if the year is a leap year
        if calendar.isleap(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Error: Invalid input for year or month.")

# Main function
def main():
    print("Math, Date-Time & Calendar Operations\n")

    # Perform mathematical operations
    math_operations()

    # Perform date-time operations
    date_time_operations()

    # Perform calendar operations
    calendar_operations()

# Execute main function
if __name__ == "__main__":
    main()




