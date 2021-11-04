#declaration de fonction qui compte le chiffre 
def funct(n): 
    if n < 10: 
       return 1 
    else: 
#la recursivite 
       return 1 + funct(n//10) 
n = int(input("entrer un nombre :")) 
#appel de fonction 
print("cette nombre",n,"contient",funct(n) , "chiffre")
