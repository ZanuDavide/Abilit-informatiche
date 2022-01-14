infile='data.txt'

indata=open(infile, 'r')
linee=indata.readlines()
indata.close()
x=[]
y=[]
for el in linee:
  valori=el.split()
  x.append(float(valori[0]))
  y.append(float(valori[1]))
print(x+y)