
#declaration d'une fonct qui calcule le factoriell Ex : 4! = 4*3*2*1 
def factoriel(n): 
    if n == 0 : 
       return 1 
    else : 
       return n*factoriel(n-1) 
# declaration d'une funct qui calcule la somme des series 1!/1 + .... + n!/n 
def sum(y): 
    n = 0 
    for i in range(1,y+1): 
       n += factoriel(i)/i 
    return n 
y = int(input("entrer une valeur :")) 
# appel de la fonction 
print("la somme de la serie est :" , sum(y))
