fin = open('input.txt','r')
a=[]
for line in fin.readlines():
  a.append( [ int (x) for x in line.split(',') ] )

print(a)