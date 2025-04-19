# STRING CASTING

# 1. integer to string

age = 20
age_str = str(age)
print("Age (string):", age_str)
print("Type:", type(age_str))  # <class 'str'>

# 2. float to string 

height = 5.7
height_str = str(height)
print("Height (string):", height_str)
print("Type:", type(height_str))

# 3. list to string

fruits = ["apple", "banana", "cherry"]
fruits_str = str(fruits)
print("Fruits (string):", fruits_str)
print("Type:", type(fruits_str))

# 4. tuple to string

my_tuple = (1, 2, 3)
tuple_str = str(my_tuple)
print("Tuple (string):", tuple_str)
print("Type:", type(tuple_str))

# 5. dictionary to string

person = {"name": "Ayesha", "age": 20}
person_str = str(person)
print("Dictionary (string):", person_str)
print("Type:", type(person_str))

# 6. set to string

my_set = {1, 2, 3}
set_str = str(my_set)
print("Set (string):", set_str)
print("Type:", type(set_str))

# 7. boolean to string

is_student = True
student_str = str(is_student)
print("Student (string):", student_str)
print("Type:", type(student_str))

# 8. bytes to string

my_bytes = b"hello"
bytes_str = str(my_bytes)
print("Bytes (string):", bytes_str)
print("Type:", type(bytes_str))

# 9. none to string

nothing = None
none_str = str(nothing)
print("None (string):", none_str)
print("Type:", type(none_str))

# 10. objest to string

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"

obj = Student("Ayesha")
obj_str = str(obj)
print("Object (string):", obj_str)
print("Type:", type(obj_str))

# 11. object f-string

name = "Ayesha"
age = 20
height = 5.4
print(f"Name: {name}, Age: {str(age)}, Height: {str(height)}")

# 12. unicode to string
unicode_str = "\u03A9"  # Omega symbol
print("Unicode (string):", unicode_str)
print("Type:", type(unicode_str))

