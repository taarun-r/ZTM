# Chapter 80 & 81

# Clean code
# Readability
# predictability
# DRY - Dont repeat yourself 

# Chapter 81


lower_case= ["a", "b", "c", "d", "e", "f", "g", "h", "h", "i", "j", "j"]

dup = []


for x in lower_case:
    if lower_case.count(x) >1:
        if x not in dup:
            dup.append(x)
print(dup)
    