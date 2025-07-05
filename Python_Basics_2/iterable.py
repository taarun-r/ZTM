# Chapter 72 - Iterable
# iterable - can be a list, dictionary, tuple, set, string - these can be iterated ->one by one check each item in the collection.
# int cannot be iterable

user = {
    "name": "Golem",
    "age" : 5000,
    "can_swim" : False
}
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item) 

for item in user.items():
    key, value = item ;
    print(key, value)
# Short hand way 

for key, value in user.items():
    print(key, value)




# for item in (1,2,3,4,5,6):
#     for letters in ["a", "b", "c", "d", "e", "f"]:
#         print(item, letters)