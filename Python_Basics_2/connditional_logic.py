# if and else codintions & elif , "and"
# elif can be multiple

is_old = True
is_licenced = True

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