# Chapter 70 
# is vs ==
#  == checks for equality & value
# " is"  check the location in memory where it is stored the same 
# Data structures like dict, set, tuple, sets will always be false since they are stored in a different memory location

print(True == 1)   # True
print("" == 1)     # False
print([] == 1)     # False
print(10 == 10.0)  # True
print([] == [])    # True


print(True is 1)   # False
print("" is 1)     # False
print([] is 1)     # False
print(10 is 10.0)  # False
print([] is [])    # False