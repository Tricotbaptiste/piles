def creer_piles2(c):
    p=[None]*(c+1)
    p[0]=0
    return p
def empiler2(p,x):
    p[p[0]+1] = x
    p[0]= p[0]+1
    return p 
def depiler2(p):
    p[p[0]]=None    
    p[0]=p[0]-1
    return p
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
    for i in range (p[0]):
        p2[i]=p[p[0]-1]
    return p2
    