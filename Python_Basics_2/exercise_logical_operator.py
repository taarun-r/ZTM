is_magician = False
is_expert = True

# if is_magician and is_expert:
#     print("You are a master magician")
# elif is_magician != is_expert:
#     print("At least your getting there")
# elif is_expert != is_magician:
#     print("You need magic powers")
# else: 
#     print("You need to practice more ")


if is_expert and is_magician:
    print("Your are a master")
elif is_magician and not is_expert:
    print("you need to get there")
elif not is_magician:
    print("You need powers")