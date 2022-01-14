import sys

param1=input()
param2=input()

sum1=param1+param2
#interpreta i due parametri come stringhe, non numeri. quindi vanno convertiti
print(type(param1))


print('somma1=', sum1)

#li rendo dei numeri

sum2=float(param1)+float(param2)

print('somma2=', sum2)