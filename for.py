


for i in range(1,9):
  print(i+1)
else: 
  print('loop stop')

  #si ferma al 9 escluso


a=[1,2,3,4,5]
y=int(input('scrivi un numero:'))

for y in a:
  print('trovato')
  break #senza il break ripete il processo per piu di una volta finche non trova y
else:
  print('non esiste')


for el in a:
  print(el)
  a.remove(el)
  print(a)