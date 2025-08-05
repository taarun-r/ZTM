# CH89 Clean code 

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
print (is_even(67))


####################################################################

# Clean Code 1 

def is_even(num):
    if num % 2 == 0:
        return True
    # elif num % 2 != 0:
    #     return False
    else:
        return False

print (is_even(67))

####################################################################
# Clean Code 2

def is_even(num):
    if num % 2 == 0:
        return True
    # elif num % 2 != 0:
    #     return False
    # else:
    return False

print (is_even(67))

####################################################################
# Clean Code 3

def is_even(num):
    return num % 2 == 0
print (is_even(67))