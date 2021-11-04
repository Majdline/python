def find_position(x): 
     for i in range(len(l)):
        for j in range(len(l[0])): 
           if l[i][j] == x : 
               return print("la position de ce element est :",i,j)
     else: 
          print("cette valeur n'existe pas dans le matrice") 
l = [[1,2,3,4],[5,6,7,8]] 
n = int(input("Entrer une valeur :")) 
find_position(n)
