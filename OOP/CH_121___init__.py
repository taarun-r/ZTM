# Chapter 122  __init__


class PlayerCharacter:
    membership = True    # This is called a class object attributes , this is not dynamic but static 
    def __init__(self, name = "anonymous", age = 0):
        if (age > 18):
            self.name = name  #attributes
            self.age = age

    def shout(self):      # run is a method 
        print(f"My name is {self.name}")

player1 = PlayerCharacter("Brady", 11)

print(player1.membership)
