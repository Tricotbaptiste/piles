from piles import *
p1 = creer_piles2(5)
empiler2(p1,'A')
empiler2(p1,'B')
empiler2(p1,'C')
empiler2(p1,'D')

vider_pile(p1)

empiler2(p1,'A')
empiler2(p1,'B')
empiler2(p1,'C')
empiler2(p1,'D')
depiler2(p1)
print(p1)
p2 = creer_piles2(5)
inverse_pile3(p1)
