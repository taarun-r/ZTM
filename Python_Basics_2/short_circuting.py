# Short circuiting in Python
# Example for short-circuiting in Python is when using or where it will not evaluate the second condition if the first one is True.

is_Friend = True
is_User = False

# if is_Friend and is_User  # True if both are True
#     print(is_Friend and is_User)  # Output: True

if is_Friend or is_User:  # True if at least one is True
    print(is_Friend or is_User)  # Output: True