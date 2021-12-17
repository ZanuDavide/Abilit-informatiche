

a=['ciao','come','stai?']
c=['tutto','bene','tu?']
print('operazioni di base')
print(a[0],a[2],a[0:3])
print(len(a))
print(a+c,a*2)



print('slicing')
b=[0,1,2,3,4,5,6,7,8,9,'pi']
print(b[0:6:2]) #di due in due, non conta sesta parola
print(b[1::2], b[1::], b[::]) #:: serve per dire fino alla fine
print(b[6:1:-2])#di due in due al contrario

print('main functions with lists')
l1=[1,2,3,4,5,2,10]
l2=[1,3,5,7,1]

print(max(l1),max(l2),min(l1),min(l2))
l1.insert(1,'nuovo')
l1.append('ciao')
print(l1)

l2.pop(3)
l2.remove(1) #lo rimuove solo una volta
print(l2)
print(l1.count(4), l1.count(2), l1.index(10))

print('uso di range')
x_range=range(1,10)
print(type(x_range))
x_list=list(x_range) #devo convertire range in list
print(type(x_list))
print(x_list)
x_list.pop() #senza nulla elimina ultima ogg della list
x_list.pop(0)
print(x_list)

print('membership')
a=4
for a in l1:
  print('true')
  break














