#declaration d'une function de Fibonacci 
def fibonacci(a): 
    if a in [0,1]: 
       return a 
    else: 
       return fibonacci(a-1) +fibonacci(a-2) 
a = int(input("Entrer une valeur :")) 
print("la serie de fibonacci est :",end=' ') 
list = [fibonacci(i) for i in range(a)] 
for i in list: 
#imprimer la serie dans un ligne 
   print(i , end=' ')
