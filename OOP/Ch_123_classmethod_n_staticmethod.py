# Chapter 124 : Class Methods & static methods 

class PlayerCharacter:
    membership = True
    def __init__(self, name , age ):
        self.name = name
        self.age = age 
    
    def shout(self):
        print(f" my name is {self.name}")

    @classmethod
    def add_stuff(cls, num1 , num2 ):
        return num1 + num2 
    
    @staticmethod
    def add_more(num1, num2):
        return num1 + num2 
    

player1 = PlayerCharacter("Tom" , 20)

print(player1.shout())

print(player1.add_stuff(5,6))


player3 = PlayerCharacter.add_stuff (4,5)
print(player3)