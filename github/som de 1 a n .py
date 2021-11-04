#Declaration d'une fonction qui calcule la somme de 1 jusqu'a n 
def som(n): 
    if n == 1 : 
       return 1 
    else: 
#la récursivité 
       return n + som(n-1) 
y = int(input("Entrer une valeur :")) 
#appel du fonction 
print("la somme de 1 jusq'a ",y ,"est :" ,som(y))
