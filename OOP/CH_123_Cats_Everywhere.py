# CH - 123 : Cats everywhere exercise 

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age




# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("milly", 3)
cat2 = Cat("Kandu", 7)
cat3 = Cat("sheeba", 4)

# 2 Create a function that finds the oldest cat

def OldestCat(*args):
    return max(args)
            
    



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"Oldest cat is {OldestCat(cat1.name, cat2.name,cat3.name)}")
print(f"Oldest cat is {OldestCat(cat1.age, cat2.age,cat3.age)} years old")