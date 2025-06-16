# Dictionary Methods

user = {"basket": [1, 2, 3], "greet": "hello", "age": 20}
# print (user["age"])

print(user.get("age", 55))

# get is a method of the object on dictionary
# Can be used to avoid errors


#  Not a common way to create dict

user2 = dict(name="John")
print(user2)
