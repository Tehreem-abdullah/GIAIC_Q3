# list are used to store multiple items in a single variable.
# List are created using square brackets [].
# List items are ordered, changeable and allow duplicate valuse.
#Example

thislist = ["apple", "banana", "cherry"]
print(thislist)
#List items are odered changeable and allow duplicate values.

#list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list items - Data types
list1 = [ "ali", "ahmed", "adnan"]
list2 = [ 1,2,3,4,5]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thislist = list(("apple","mango","strwaberry"))
print(thislist)

#Access Items
thislist = ["Pakistan", "India", "Bangladesh"]
print(thislist[1])

#Negative Indexing
thislist = ["Pakistan", " India", "Bangladesh"]
print(thislist[-1])

#Range of Indexes
thislist = ["pakistan", "bangladesh", "srilanka", "india", "nepal"]
print(thislist[2:5])

#Change Items Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Add Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Remove Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Another way to join two lists are by appending all the items from list2 into list1, one by one
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

#Use the extend() method to add list2 at the end of list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Creating a tuple
my_tuple = (5, 10, 15, 20, 25)
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
print("First Element in Tuple:", my_tuple[0])
print("Last Element in Tuple:", my_tuple[-1])

# Slicing a tuple
sub_tuple = my_tuple[1:4]
print("Sliced Tuple:", sub_tuple)

# Iterating through a tuple
print("Iterating through tuple:")
for item in my_tuple:
    print(item)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)

# Finding the length of a tuple
print("Length of Tuple:", len(my_tuple))

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements to a set
my_set.add(6)
print("After Add:", my_set)

# Removing elements from a set
my_set.remove(3)
print("After Remove:", my_set)

# Checking membership
print("Is 2 in set?", 2 in my_set)

# Iterating through a set
print("Iterating through set:")
for item in my_set:
    print(item)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Creating a frozenset
my_frozenset = frozenset([10, 20, 30, 40, 50])
print("Original Frozenset:", my_frozenset)

# Checking membership in frozenset
print("Is 20 in frozenset?", 20 in my_frozenset)

# Iterating through a frozenset
print("Iterating through frozenset:")
for item in my_frozenset:
    print(item)
