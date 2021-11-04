#Declaration d'une function qui divise une liste en 3 morceaux égaux et inverser chaque morceau
def div(l): 
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(l)):
        if i < 3:
            l1.append(l[i])

    for j in range(3,len(l)):

        if j < 6:
            l2.append(l[j])

    for k in range(6,len(l)):

        if k < 9:
            l3.append(l[k])

    return print(l1[::-1] , l2[::-1] ,l3[::-1])
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#appel du fonction
div(list) 