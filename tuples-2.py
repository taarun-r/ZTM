my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:4]
print(new_tuple)  # Prints the sliced tuple (2, 3, 4)

# Tuples has only two methods: count and index
# Count - Returns the number of occurrences of a specified value in the tuple
print(my_tuple.count(2))  # Prints the number of occurrences of 2 in the tuple
print(my_tuple.index(4))  # Prints the number of occurrences of 6 in the tuple (0, since 6 is not in the tuple)