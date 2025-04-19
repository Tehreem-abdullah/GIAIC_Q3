# EXCEPTION & HANDLING
# 1. Exception handling
# 1.1 try block
# 1.2 except block
# 1.3 finally block
# 1.4 else block
# 1.5 putting it all together

# 1.1 try block
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
finally:
    # This block will always execute
    print("This will always execute).")

# 1.2 except block
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
finally:
    # This block will always execute
    print("This will always execute).")

# 1.3 finally block
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
finally:
    # This block will always execute
    print("This will always execute).")

# 1.4 else block
try:
    # Code that may raise an exception
    result = 10 / 2  # This will not raise an exception
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
else:
    # This block will execute if no exception occurs
    print("Result:", result)
finally:
    # This block will always execute
    print("This will always execute).")

# 1.5 putting it all together
try:
    # Code that may raise an exception
    result = 10 / 2  # This will not raise an exception
except ZeroDivisionError as e:
    # Handle the exception
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
else:
    # This block will execute if no exception occurs
    print("Result:", result)
finally:
    # This block will always execute
    print("This will always execute).")
    