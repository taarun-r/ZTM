# dictionary - its a data type and a data structure, its a way for us to organise the data | Its a key value pair and is unordered
# As long as we know the key the PC will know where to look for it | The key vaule pair can be anything, like and list / string or boolean
# In other languages they may be called as a hash table or a map or object in python it is refered to a disctionary (dict)
# dictionarys are containors around data 



# dictionary ={
#     "a" : 1,
#     "b" : 2,
#     "x" : 3,
# }
# print(dictionary["b"])


mixed_data ={
    "a" : [1,2,3],
    "b" : "hello",
    "x" : True
}
print(mixed_data["a"][1])


my_list = [
    {
    "a" : [1,2,3],
    "b" : "hello",
    "x" : True
    },
    {
    "a" : [4,5,6],
    "b" : "hello",
    "x" : True
    }
]
print(my_list[0]["a"][2])