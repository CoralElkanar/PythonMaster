# ******************************************************************************************

"""
Lists:
- can contain the values belonging to different data types (heterogeneous)
- mutable
"""

# positive indexing:
x = [0,1,2,3,4]

# negative indexing:
y = [-5,-4,-3,-2,-1]

length = len(x)   # n = 5
print(f"the length of x={x} is {length}")

# Append object to the end of the list.
x.append(5)
print(f"x = {x}, after adding '5' to the end of the list")

# Remove first occurrence of value.
# Raises ValueError if the value is not present.
x.remove(5)
print(f"x = {x}, after removing the first occurrence of the value '5'")

# Return a shallow copy of the list.
z = x.copy()
print(f'z = {z}, is a copy of x')

# Return first index of value.
# Raises ValueError if the value is not present.
index_of_val_2 = x.index(2)
print(f"index of the value '2' in x is {index_of_val_2} ")

# Insert object before index.
x.insert(0,4)
print(f"x = {x}, added the element '4' in the spot before the index '0'")
print(f'z = {z} has remained unchaneged')

# Return number of occurrences of value.
count_of_val_4 = x.count(4)
print(f"count of the value '4' in x is {count_of_val_4}")

# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
element_popped = x.pop(0)
print(f"the element we popped from the list at the index 0 is: {element_popped}")
print(f"x = {x}, we popped the element in index 0")

# Extend list by appending elements from the iterable.
x.extend([12,13])
print(f"x = {x}, after extending [12,13]")

# reverse the list
x.reverse()
print(f"x = {x} after reversing")

# sort the list in its place
x.sort()
print(f"x = {x} sorted")

# clear the list
x.clear()
print(f"x = {x}, after clearing x")
print(f"z = {z}, stays the same")


# ******************************************************************************************

"""
Tuples:
- can have heterogenous data types in them
- NOT mutable
- faster than lists
"""

t = (10, 20, 40.5, 'hello', 4+5j, 10)

# access values in the tuple - reffering the index we want to acess
print(t[1])  # 20

# Return number of occurrences of value.
count = t.count(10)
print(f"count of the value '10' in the tuple is {count}")

# Return first index of value.
# Raises ValueError if the value is not present.
index_of_val_20 = t.index(20)
print(f"the index of the first occurence of the element '20' is {index_of_val_20}")


# ******************************************************************************************

"""
Dictionary:
- Hold key:value pairs
- mutable
"""

d = {'key_a':100, 'key_b':200, 'key_c':300}

# a shallow copy of the dictionary
d2 = d.copy()
print(f"created d2 - a copy of d: {d2}")

# add another pair of key:value to the dictionary
d['key_e'] = 50
print(f"the dictionary after adding 'key_e':50 is {d}")

# a set-like object providing a view on D's items
d_items = d.items()
print(f"d.items() -> {d_items}")

# a set-like object providing a view on d's keys
d_keys = d.keys()
print(f"d.keys() -> {d_keys}")

# an object providing a view on D's values
d_values = d.values()
print(f"d.values() -> {d_values}")

# Retur n the value for key if key is in the dictionary, else returns default.
val_for_key_b = d.get('key_b', 'default')
print(f"value for the 'key_b' is {val_for_key_b}")

#  remove specified key and return the corresponding value. 
# If key is not found, d is returned if given, otherwise KeyError is raised
value_of_key_pop = d.pop('key_c')
print(f"the dictionary after removing 'key_c':{value_of_key_pop} is {d}")

# 
item_popped = d.popitem()
print(f"the dictionary after removing {item_popped} is {d}")

# # Create a new dictionary with keys from iterable and values set to value.
# d.fromkeys()



# ******************************************************************************************

"""
Sets:
- unordered collection of unique elements - no duplicates in the list
- we cannot fetch a value by an index position, we can only check whether that value exists in the set or not.  
- mutable
"""

s = {10,30,50,4,4,5,99}

print(f"the set we created - {10,30,50,4,4,5,99} will delete all duplications: s={s} ")

# Return a shallow copy of a set.
s2 = s.copy()
print(f"vreated s2 = {s2} as a copy of s")

# Add an element to a set.
# This has no effect if the element is already present.
s.add(17)
print(f"s after adding 17 to it - {s}")

# Remove an element from a set if it is a member.
# If the element is not a member, do nothing.
s.discard(10)
print(f"s after removing 10 - {s}")

# Return the intersection of two sets as a new set.
# (i.e. all elements that are in both sets.)
intersection = s.intersection(s2)
print(f"the set of intersection between s={s} and s2={s2} is {intersection}")

