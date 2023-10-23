from Classes.Player import Player
from Classes.Rune import Rune, Rune_Defense


R1 = Rune_Defense(1)
R2 = Rune_Defense(2)
P = Player("P1",1,20,5)
P.Tatooes(1, R1)
P.Tatooes(2, R2)
P.Tatooes(3, R1)
print(P.lp)
P.TakeDamage(10)
print(str(P.Rune1.rune_type) + str(P.Rune1.strength))
print(str(P.Rune2.rune_type) + str(P.Rune2.strength))
print(str(P.Rune3.rune_type) + str(P.Rune3.strength))
print(P.lp)
input('PAUSE')

