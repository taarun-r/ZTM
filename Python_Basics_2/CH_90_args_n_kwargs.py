# CH-90 args and kwargs
# args : arguments
# kwargs : key word arguments

# *args & **kwargs

#  args
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))


# kwargs

def super_func(*args, **kwargs):
    print(kwargs)
    for items in kwargs.values():
        total += items 
    return sum(args) + sum()

print(super_func(1,2,3,4,5, num1=5, num2 = 10 ))