# CH_92 : Walrus Operator " := "



b = "Hellooooooo"
# if (len (b) > 10):
#     print(f" Too long {len(b)} elements")


if ((n := len(b))) > 10:
    print(f" Too long {n} elements")


while ((n:= len(b)) > 1):
    print(b)
    b = b[: -1]