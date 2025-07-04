# if and else conditions & elif , "and"
# elif can be multiple

is_old = True
is_licensed = True

if is_old:
    print("Your are old enough to drive ")
elif is_licensed:
    print("You can drive now !")
else:
    print("check check !")

if is_old and is_licensed:
    print("Your are old enough to drive and have a license")

else:
    print("check check !")