# CH 95 Scope Rules 
# Scope - What variables do I have access to 

a = 1 


def confusion():
    a = 5
    return a 

print(a)
print(confusion())


# 1 - Starts with local scope 
# 2 -  Parent local scope will be looked 

def parent():
    a= 10
    def confusion():
        return a 
    return confusion()

print(parent())
print(a)

# 1 - Starts with local scope 
# 2 -  Parent local scope will be looked 



# 3 - Global : it check the file 

def parent(): # Global rule for scope 
    # a= 10
    def confusion():
        return a 
    return confusion()

print(parent())
print(a)

# 4 - Built in python functions 

def parent(): 
    def confusion():
        return sum
    return confusion()

print(parent())
print(a)
