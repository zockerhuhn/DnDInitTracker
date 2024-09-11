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
                newMaxhp = []
                for i in maxhp.split('+'):
                    if '-' in i:                            #turn string into a list with each part of the equation seperated
                        for x in i.split('-'):
                            if i.split('-').index(x) != 0:
                                x = "-" + x
                            else:
                                x = "+" + x
                            if 'd' in x:                    #simulate dice roll
                                result = 0
                                for y in range(abs(int(x.split('d')[0]))):
                                    result += random.randint(1,int(x.split('d')[1]))
                                x = x[0] + str(result)
                            newMaxhp.append(x)
                    else:
                        if 'd' in i:                        #simulate dice roll
                            result = 0
                            for y in range(abs(int(i.split('d')[0]))):
                                result += random.randint(1,int(i.split('d')[1]))
                            i = str(result)
                        newMaxhp.append("+" + i)
                endresult = 0
                for i in newMaxhp:
                   endresult += int(i)
                self.maxhp = str(endresult)
            else:
                self.maxhp = maxhp
            if hp == 0:
                self.hp = int(self.maxhp)
            else:
                self.hp = hp
    def __str__(self):
        return f"{self.name}, {self.player}, {self.tag}, {self.initiative}, {self.hp}, {self.maxhp}"