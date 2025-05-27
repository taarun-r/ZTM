# # selfish = "01234567"
# # #  01234567
# # selfish = "8"

# # print(selfish)


# # greet = "Hello, World!"

# # # print(greet[0:9])

# # print(greet[0 : len(greet)])


# # quotes = "to be or not to be"
# # # print(quotes.capitalize())
# # # print(quotes.find("not"))
# # # print(quotes.replace("be", "he"))
# # print(quotes)
# ###############################################
# # List slicing
# #  Is an ordered sequence of objects
# # List are denoted by [] - They are collection of items - List are first of the data structures
# # In Python Lists are a form of arrays
# # Data structures are a container around your data
# # List are mutable
# shop_cart = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # print(shop_cart[0:10])

# # List Slicing [:] - is a copy of a list
# shop_cart[0] = "pineapple"
# print(shop_cart)

# # Matrix  - Is an array with another array inside of it

# # These come up in machine learning and image processing

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][2])

# # List Methods

# # To use menthods on a list you need tyo use a . after the list
# # Append and insert modifies the list in place, but does not make a copy of the list or return anything

# basket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(basket))

# # Adding to a list
# # basket.append(20)
# # new_list = basket
# # print(basket)
# # # print(new_list)

# # Insert
# basket.insert(10, 11)

# # Extend method

# basket.extend([12, 13, 14, 15])

# # Removing Method // pop is for index removal
# basket.pop()  # Removes the last item
# basket.pop(0)  # Removes the item at index 0

# # Remove method is used for removing a value from a list

# basket.remove(11)

# # Clear method 

# basket.clear() - # removes what ever is there in the lists.

# # **********************************************************
#  List Methods 2 
# new_basket = [1,2,3,4,5]
# basket  = ["a","b","c","d","e","g","x","i","f"]
# print(basket.index("d", 0, 4))

# print("e" in basket) # "in" keyword 

# print(basket.count("d"))

# List Methods 3 
# basket.sort()
# print(basket)

# Sorted - Produces a new array (Creates a new copy of the array/list)
# print(sorted(basket))

# Reverse method 
# basket.sort()
# basket.reverse()
# print(basket)

# Common List Patterns 
# print(basket[::-1])

# print(list(range(101)))

# join method 
sentence = " "
# new_sent = sentence.join(["Hi", "my", "name", "King6"])
new_sent = " ".join(["Hi", "my", "name", "King6"])
print(new_sent)
