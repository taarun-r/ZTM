# Chapter 75 

# for i,char in enumerate("Helloooo"):
#     print(i,char)


# for i,char in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]): # List 
#     print(i,char)


# for i,char in enumerate((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)): # Tuple example 
#     print(i,char)

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f"Index of 50 is: {i}")