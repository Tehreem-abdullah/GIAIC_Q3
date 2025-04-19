# CONTROL FLOW & LOOPS
# 1. if statement
x = 10
if x > 0:
    print("Positive number")

# 2. if-else statement 
x = -5
if x >= 0:
    print("Non-negative number")
else:
    print("Negative number")

# 3. if-elif-else statement
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# 4. nested if statement
x = 10 
y = 5
if x > 0:
    print("positive number")
    if y > 0:
        print("both numbers are positive")
    else:
        print("x is positive, y is not")

# 5. while loop 
i = 0
while i < 5:
    print(i)
    i += 1

# 6. for loop
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)


# 7. for loop with range
for i in range(5):
    print(i)

# 8. break loop 
i = 0 
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# 9. conrtinue loop 
i =0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

# 10. pass statement
for i in range(3):
    if i == 1:
        pass  # Does nothing
    print(i)

