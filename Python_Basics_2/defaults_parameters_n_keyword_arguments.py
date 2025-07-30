# Chapter 84 - Default Parameters and Keyword Arguments


# Positional Parameters 

def say_hello(name, emoji):
    print (f"Hello & How are you ? {name} {emoji}")


# Positional Arguments

say_hello("Taarun", ":P ")

# # Keyword Arguments Example

say_hello(emoji=" ^-^ ", name=" DeeDee ")


# Default Parameters 

def say_hello(name= "El-Demon", emoji=" :$ "):
    print (f"Hello ! {name} {emoji}")

say_hello()
say_hello("Tommy")