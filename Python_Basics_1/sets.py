# Set : Unorder collections of unique objects 
# sets are created with { }
# in a set there is no duplicates
# from a list we can convert a set using the "set" function
# Set does not support indexing 
my_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set.add(10)
print(my_set)

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)