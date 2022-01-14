l = []
a=[]
with open('input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
      l.append(map(int, line.split(',')))
      a.append(list(map(int, line.split(','))))
  
print('senza list:' ,l)
print('con list:' ,a)

#questo 'map' senza 'list' da come poutput qualcosa di strano,