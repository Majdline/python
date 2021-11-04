def cle(list , dict): 
    l = []
    l.extend(dict.values()) #add all the elements of an iterable to the end of the liste 
    new_list = [] 
    for i in list: 
        for j in l: 
            if i == j : 
             new_list.append(i) 
        return new_list 
l = [47, 64, 69, 37, 76, 83, 95, 97] 
dict1 = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97} 
print(cle(l , dict1))

