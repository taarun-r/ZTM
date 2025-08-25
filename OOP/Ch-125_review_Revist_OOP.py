# OOP Chapter 126 Developer Fundmentals

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name 
        self. age = age 
        
    def run(self):
        return self
        
player1 = PlayerCharacter("Jimmy", 55)

print(player1.run())
