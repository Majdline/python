#declaration d'une function qui changer un list vers un dict
def chang_dictio(l): 
    dic = {}
    for i in l:
 #calculer combien des fois un elemets repeter dans la liste       
        y = l.count(i) 
        dic[i] = y
    return dic
list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#appel du fonction
print(chang_dictio(list))