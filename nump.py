import numpy as np


print("creazione array")
list1=[1,2,3,4]
tupla=(4,3,2,1)

a1=np.array(list1)
a2=np.array(tupla)
a3=np.array([2,3,4,5])
a4=np.array([[1,2,3],[3,4,5]])
a5=np.array([list1,tupla])
a6=np.arange(1,6)
a7=np.arange(1,6,2)
#terzo numero in a7 sono gli step dell'arange come gia visto

print(a1,a2,a3,a4,a5,a6,a7)

print("glossary per array")

b=np.array([[1,2],[1,2]])
print(b.shape , b.size)
c=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(c.shape, c.size)
#facendo lo shape il risultato per c è (3,4) quindi il primo elemento rappresenta il numero di vettori colonna/riga e il secondo numero rappresenta il numero di elementi per ogni vettore (quindi la dimensiomne del vettore)

print("broadcasting")

s1=np.array([1,2,3])
s2=np.array([[1,2,3],[1,2,3]])
print(s1+s2) 
#è stata aggiunta la riga [1,2,3] all'array s1 dal broadcasting

p1=np.array([1,2,3,4])
p2=np.array([[1,2,3],[1,2,3]])
#print(p1+p2)
#in questo caso non è possibile il broadcasting perchè p1 ha il vettore di dimensione 4 mentre p2 ha 2 vettori di dimensione 3

print("vectorization")
pi=np.pi
a=np.array([0,pi,2*pi])
sina=np.sin(a)
print(sina)

print("matrix")

ma=np.matrix([[1,2],[3,3]])
mb=np.matrix([[1,2],[0,1]])
mdiag=np.matrix([[1,0],[0,2]])
print(ma*mb)

from numpy import linalg

print(np.linalg.eigvals(mdiag))
print(np.linalg.eigvals(ma))
print(np.linalg.eig(ma))

print("slicing")

print(ma[0,0],ma[0,1],ma[1,0],ma[1,1])
#in [a,b] a rapresenta la riga mentre b la colonna (indicizzazioine parte da 0)
print(ma[:,1])

print("reshape")
a=np.arange(1,9)
ar1=a.reshape((4,2))
ar2=a.reshape((2,2,2))
print(ar1,ar2)
#nel fare il reshape devo mantenere la size invariata, quindi un a.reshape((4,3)) non sarebbe possibile 

print("plot")

import matplotlib.pyplot as plt

t=np.arange(0.0, 2.0, 0.01)
s=1+np.sin(2*np.pi*t)
plt.plot(t, s)
plt.xlabel('time s')
plt.ylabel('voltaggio mV')
plt.title('voltaggio sinusoidale')
plt.grid(True)
plt.savefig("plot1.png")
plt.show()