# CH 121 Attributes and Methods (ZTM)

class PlayerCharacter:
    membership = True    # This is called a class object attributes , this is not dynamic but static 
    def __init__(self, name , age):
        self.name = name  #attributes
        self.age = age

    def run(self):      # run is a method 
        print("run")
        return "done"

player1 = PlayerCharacter("Cinday", 41)
player2 = PlayerCharacter("Manday", 21)
player2.attack = 50



print(player1.membership)
print(player2.membership)

