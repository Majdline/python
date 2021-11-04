#declartion d'un funct qui convertir le nombre décimal en nombre binaire 
def binaire(n): 
    if n == 0 : 
        return 0 
    else: 
        return n%2 + (10*binaire(n//2)) 
n = int(input("entrer la valeur de n :")) 
#appel du function 
print("le binaire de la valeur ",n ,"est :" ,binaire(n))
