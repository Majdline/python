# éléments d'index impair dans la première liste et les paires dans la deusieme
def index(l1,l2):
     l3= []
     for i in range(len(l1)):
      if i%2 != 0 :
        l3.append(l1[i])
     for j in range(len(l2)):
      if j%2 == 0:
         l3.append(l2[j])
     return l3
list1 = [3, 6, 9, 12, 15, 18]
list2 = [4, 8, 12, 16, 20, 24, 28]
#appel de fonction 
print(index(list1,list2))
