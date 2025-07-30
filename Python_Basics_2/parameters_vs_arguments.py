# Chapter 83
# Arguments Vs Parameters 

# Parameters are part of the the functions they can be a variable  ( Defines the fuctions )
# Parameters allow us to give the function when we call it the Arguments

def say_hello(name, emoji):
    print (f"Hello ! {name} {emoji}")


# Arguments are used as the actual vaules used in fuctions (Calls the function)

say_hello("Jinny", ":P ")
say_hello("Henny", "<3 ")
say_hello("Johnny", " :) ")

# # Keyword Arguments Example

say_hello(emoji=" ^-^ ", name=" DeeDee ")


# Default Parameters 

def say_hello(name= "El-Demon", emoji=" :$ "):
    print (f"Hello ! {name} {emoji}")

say_hello()
say_hello("Tommy")