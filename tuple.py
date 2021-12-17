
print('operazioni di base')

tup1="a","b","1","6","30"
tup2=(1,2,3,'ciao','hi')
tupvoid=()
tup3=(50,)
tup4=(50)
print(tup3,tup4,tupvoid) 

print(tup1[2],tup1[1:3],tup1[0:3],tup1[0:5:2])

#del(tup1)
#print(tup1)
#delete tup1 la elimina comunque

print('conversione list, tuple')
rng=range(1,7)
tupr=tuple(rng)
lstr=list(rng)
print(type(tupr),type(lstr))
