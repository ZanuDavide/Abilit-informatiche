a='Ciao a tutti'
b="come state?"

print("prima lettera:", a[0])
print("prime 3 lettere:", a[0:3])
#facendo [0:3] lui scrive la 0,1,2 ma non la 3

print(a+a)
print(a*2)
print(a+" "+b)


nome="davide"
print("Ciao %s" %nome)
print(nome)
print(r'nome')

print(a.replace('i', '1'))
print(a.replace('i', '1', 1))
print(a.strip('C'))
print(a.strip('c')) #differenza tra caps e no!