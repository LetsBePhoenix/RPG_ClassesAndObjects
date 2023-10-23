from Classes.Rune import Rune


class Player():
    def __init__(self, name:str, lvl:int, lp:int, strg:int):
        self.name = name
        self.lvl = lvl
        self.lp = lp
        self.strg = strg
        self.Rune1 = Rune(None)
        self.Rune2 = Rune(None)
        self.Rune3 = Rune(None)

    def Tatooes(self, ToChange:int, Item:Rune):
        if (ToChange == 1):
            self.Rune1 = Item
        elif (ToChange == 2):
            self.Rune2 = Item
        else:
            self.Rune3 = Item
    


    def TakeDamage(self, ammount):
        # Berechne den Schaden / Abzug durch die Ruhnen
        if (self.Rune1.rune_type == "Defense"):
            ammount -= self.Rune1.strength
        if (self.Rune2.rune_type == "Defense"):
            ammount -= self.Rune2.strength
        if (self.Rune3.rune_type == "Defense"):
            ammount -= self.Rune3.strength
        # Füge dem spieler schaden zu
        if (ammount > 0):
            self.lp -= ammount


    def DealDamage(self, ammount, life_from_opponent):
        # Berechne den dem gegner zugefügten schaden
        if (self.Rune1.rune_type == "Strenght"):
            ammount += self.Rune1.srenght
        if (self.Rune2.rune_type == "Strenght"):
            ammount += self.Rune2.srenght
        if (self.Rune3.rune_type == "Strenght"):
            ammount += self.Rune3.srenght
        # Füge dem gegner schaden zu
        return ammount

