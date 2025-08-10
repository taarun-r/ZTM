# CH 96 : - Nonlocal keywords

# Scope - What variables do i have access to 
# Non local key is used to refer to the key word "Parent Local" || This is not a global variable but is out side the scope of my function


def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:",x)

outer()


# 1 - Starts with local scope 
# 2 -  Parent local scope will be looked 
# 3 - Global : it check the file
# 4 - Built in python functions 