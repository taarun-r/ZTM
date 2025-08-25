# Chapter 127 - Abstraction 

# Abstraction - means hiding of information , and giving access to only what is necessary 


class PlayerCharacter:
    def __init__(self, name , age):
        self.name = name 
        self.age = age

    def run(self):
        print("run")
    
    def speak(self):
        print(f"My Name is {self.name}, and I'm {self.age} years old ")


player1 = PlayerCharacter("Mike", 42)
print(player1.name)
player1.speak()

