# Chapter 120 - Create Your Own Objects 

#OOP

# Coding our own class 

class PlayerCharacter:          # Construction Method or 
    def __init__(self, name):
        self.name = name  # These are attributes 

    def run(self):
        print("run")

player1 = PlayerCharacter()

print(player1)