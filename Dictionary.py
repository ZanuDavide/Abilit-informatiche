print('comandi base')
dic={1:'a', 2:'b', 3:'c', 4:'d'}
dic1={'name':'davide', 'age':24 , 'sex':'male'}
print(type(dic))
print(dic[3],dic1.get('age')) #due metodi diversi

print('remove')
print(dic.pop(2))
print(dic)
dic.clear() #rimuovo tutto assieme
print(dic)
print(any(dic)) #da falso se vuoto
print(all(dic1))
print(sorted(dic1)) #da lista delle keys


