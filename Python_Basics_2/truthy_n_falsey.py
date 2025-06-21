#  Truthy vs Falsey

is_old = bool("hello")
is_licenced = bool(5)

print(bool("hello")) # Truthy value in python 
print(bool(5))# Truthy value in python 

print(bool("")) # Falsey value in python, which has a empty string 
print(bool(0))# Falsey value in python , value is zero "0"

#  Truthy vs Falsey


if is_old:
    print("Your are old enought to drive ")
elif is_licenced:
    print("You can drive now !")
else:
    print("check check !")

if is_old and is_licenced:
    print("Your are old enought to drive and have a license")

else:
    print("check check !")

password = "123"
username = "johnny"

if password and username:
    print("you can login   !")
else:
    print("you cannot login !")