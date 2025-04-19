# SETS AND FROZEN SETS

# --- Working with Sets ---

# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Adding elements
set_a.add(7)
print("Set A after adding 7:", set_a)

# Removing elements
set_a.discard(2)  # Doesn't raise error if not found
print("Set A after discarding 2:", set_a)

# Set Operations
print("Union:", set_a | set_b)           # or set_a.union(set_b)
print("Intersection:", set_a & set_b)    # or set_a.intersection(set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Membership Test
print("Is 5 in Set B?", 5 in set_b)

# --- Working with Frozensets ---

# Creating frozensets (immutable set)
frozen_a = frozenset([10, 20, 30])
frozen_b = frozenset([30, 40, 50])

# You can perform operations like union and intersection
print("Frozen Union:", frozen_a.union(frozen_b))
print("Frozen Intersection:", frozen_a.intersection(frozen_b))

# But you can't modify a frozenset (add/remove will raise error)
try:
    frozen_a.add(60)  #  This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)
