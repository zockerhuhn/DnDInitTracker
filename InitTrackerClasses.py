import random

class creature:
    def __init__(self, player:bool, name:str, tag:str, initiative:str, hp:int, maxhp:str):
            self.player = player
            self.name = name
            self.tag = tag
            if ('+' or '-') in initiative:
                self.initiative:int = random.randint(1,20)+int(initiative)
            else:
                self.initiative:int = int(initiative)
            if "d" in maxhp:
                maxhp.split("+" or "-")
    def __str__(self):
        return f"{self.name}, {self.player}, {self.tag}, {self.ac}, {self.hp}, {self.maxhp}"