# Chapter 85 : Return 

def sum(num1, num2):
    print("Hi Everyone")
    return num1 + num2
    

print(sum(21, 25))

# Function should do one thing really well and usually should return something 


def sum(num1, num2):
    # print("Hi Everyone")
    return num1 + num2
    
total = 15 
print(sum(21, total))

def sum(num1, num2):
    def some_func(n1, n2):
        return n1 + n2
    return some_func(num1, num2)

total = sum(24, 34)

print(total)

# Return keyword automatically exits the function 

