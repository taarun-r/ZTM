# Chapter 76 & 77 - While loop

i = 0  
while i < 50:
    print(i)
    i = i + 1
else:
    print("Done with all the work")


# When to use a while loop and when to use for loop 

my_list = [1,2,3]

for item in my_list:
    print(item)

i = 0 
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    answer = input("Say something :  ")
    if (answer == "bye"):
        break 