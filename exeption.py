def div(a,b):
 try:
  res= a / b
 except ZeroDivisionError:
  print("dividi per zero")
 else:
  print("risultato=", res)
 finally:
  print("executing finally clause") 


print(div(3,4))
print(div(3,0))