#Declaration d'une function qui fait l'intersection des deux sets
def inter(l1,l2): 
    a = l1.intersection(l2)
    print("l'intersection de set1 et set2 :", a)
#return les elements de la set 1 sans les element d'intersection
    return l1-a 
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
# appel du fonction
print("Set 1 après suppression : " , inter(set1,set2)) 