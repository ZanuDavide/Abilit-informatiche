a=("oggi fa","ciao","sono le")
b=("caldo", "come stai", "13.00")

x=zip(a,b)
print(tuple(x))


r=("oggi fa","ciao","sono le")
v=("caldo", "come stai", "13.00", "3")
y=zip(r,v)
print(tuple(y))
#il 3 viene ignorato, gli item in eccesso sono ignorati

