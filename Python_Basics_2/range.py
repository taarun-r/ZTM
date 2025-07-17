# Chapter 74 - range function 

print(range(100))
for num in range(0,101):
    print(num)

# If a variable is not needed the use " _ " 

for _ in range(0, 100, 2):
    print(_)

# Third parameter is a step over 

for _ in range(2):
    print(list(range(10)))