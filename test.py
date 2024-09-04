import random

maxhp = "2+18d6+8d4-5"
print(maxhp.split("+" and "-"))
print(maxhp.split("+" or "-"))
maxhp = maxhp.split("+")
for i in maxhp:
    if "-" in i:
        