def creer_piles2(c):
    p=[None]*(c+1)
    p[0]=0
    return p
def empiler2(p,x):
    p[p[0]+1] = x
    p[0]= p[0]+1
    return p 
def depiler2(p):
    valeur = p[p[0]]
    p[p[0]]=None    
    p[0]=p[0]-1
    return valeur
def pile_vide2(p):
    if p[0]== 0:
        return True
    else:
        return False
def taille2(p):
    return p[0]
def sommet2(p):
    return p[p[0]]
def vider_pile(p):
    for i in range (len(p)):
        p[i]= None
    p[0]= 0
    return p
def inverse_pile(p,p2):
    p2[0]= p[0]
    for i in range (1,p[0]+1):
        p2[i]=p[p[0]]
        p[p[0]] = p[p[0]-i]
    return p
def inverse_pile2(p,p2):
    p2[0] = p[0]
    n=0
    for i in range(1,p[0]+1):
        p2[i] = p[p[0]-n]
        n =n+1
    return p2
def inverse_pile3(p):
    p2 = creer_piles2(5)
    for i in range(p[0]):
        valeur = depiler2(p)
        empiler2(p2,valeur)
    print(p2)