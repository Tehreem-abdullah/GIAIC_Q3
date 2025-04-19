# LIST , TUPLES , DICTIONARY

# 1. Acessing list elements
# List of fruits
fruits = ["apple", "banana", "cherry", "mango", "grape"]

# Accessing elements by index
first_fruit = fruits[0]       # First element
last_fruit = fruits[-1]       # Last element
third_fruit = fruits[2]       # Third element

print(f"First fruit: {first_fruit}")
print(f"Third fruit: {third_fruit}")
print(f"Last fruit: {last_fruit}")

# Looping through the list with index
print("\nAll fruits with their index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Slicing the list
print("\nSome fruits using slicing:")
print("First two:", fruits[:2])          # ['apple', 'banana']
print("Middle fruits:", fruits[1:4])     # ['banana', 'cherry', 'mango']
print("Last two:", fruits[-2:])          # ['mango', 'grape']

# Working with nested lists
nested_fruits = [
    ["apple", "banana"],
    ["cherry", "mango"],
    ["grape", "kiwi"]
]

print("\nAccessing elements in a nested list:")
print(f"Element at [0][1]: {nested_fruits[0][1]}")   # banana
print(f"Element at [2][0]: {nested_fruits[2][0]}")   # grape
print(f"Element at [1][0]: {nested_fruits[1][0]}")   # cherry

# 2. list methods
# modifying the list
fruits.append("orange")  # Add to the end
fruits.insert(2, "kiwi")  # Add at index 2
fruits.remove("banana")  # Remove by value

fruits.pop(1)
# Remove by index (removes "kiwi" which is now at index 1)

fruits.sort() # Sort the list in ascending order 
fruits.reverse() # Reverse the list 

print("\nModified fruits list:")
print(fruits)  # ['orange', 'mango', 'kiwi', 'grape', 'cherry', 'apple']


# 3.Tuples
# Tuples are imutable, meaning they cannot be chnaged after ctreation 
# tuples are defined u8sing parentheses ()
# Example of a tuple
my_tuple = ("apple", "banana", "cherry", "mango", "grape")


# Accessing elements in a tuple 
print("\nAccessing elements in a tuple:")
print(f"First element: {my_tuple[0]}")  # apple
print(f"Last element: {my_tuple[-1]}")  # grape
print(f"Slice of tuple: {my_tuple[1:4]}")  # ('banana', 'cherry', 'mango')
print(f"Tuple length: {len(my_tuple)}")  # 5
print(f"Tuple count of 'apple': {my_tuple.count('apple')}")  # 1
print(f"Index of 'mango': {my_tuple.index('mango')}")  # 3
print(f"Tuple unpacking:")
a = my_tuple[0]
b = my_tuple[1]
c = my_tuple[2]
d = my_tuple[3]
e = my_tuple[4]
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")  # a: apple, b: banana, c: cherry, d: mango, e: grape
print(f"Tuple unpacking with multiple variables:")
a, b, c, d, e = my_tuple
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")  # a: apple, b: banana, c: cherry, d: mango, e: grape


# 4 . Dictionary
# A dictionary is a collection of key-value pairs
# Dictionaries are defined using curly braces {}
# Example of a dictionary

my_dict = {
    "name": "Tehreem",
    "age": 19,
    "city": "karachi",
    "is_student": True,
}

# Accessing values
print("\nAccessing values in a dictionary:")
print(f"Name: {my_dict['name']}")  # Tehreem
print(f"Age: {my_dict['age']}")    # 19
print(f"City: {my_dict['city']}")  # karachi
print(f"Is student: {my_dict['is_student']}")  # True

# Modifying the dictionary
my_dict["age"] = 19 # update age
my_dict["is_student"] = True # update is_student
my_dict["hobby"] = "painting" # add new key-value pair
my_dict["hobby"] = "reading" # update hobby
my_dict.pop("city") # remove city key-value pair
print("\nModified dictionary:")
print(my_dict)  # {'name': 'Tehreem', 'age': 19, 'is_student': True, 'hobby': 'reading'}

# Deleted items
print("\nDeleted items:")
print(my_dict.popitem()) # remove the last inserted item
print(my_dict) # {'name : "Tehreem", "age: 19" "is_student: "True"}
print(my_dict.clear()) # remove all items from the dictionary 
# print(my_dict) # {}  # empty dictionary

# 5. Dictionary Methods
# Getting keys and values
print("\nKeys and values in the dictionary:")
print(f"Keys: {my_dict.keys()}")  # dict_keys(['name', 'age', 'is_student'])
print(f"Values: {my_dict.values()}")  # dict_values(['Tehreem', 19, True])
print(f"Items: {my_dict.items()}")  # dict_items([('name', 'Tehreem'), ('age', 19), ('is_student', True)])

# Iterating through a dictionary
print("\nIterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")  # name: Tehreem, age: 19, is_student: True

