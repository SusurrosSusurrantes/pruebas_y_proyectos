contador=0
myEmail=input("Ingresá tu Email: ")
for i in myEmail:
	if(i== "@"  or ".com"):
		contador=contador+1

if contador==2:
	print("Pasá maquinola")

else:
	print("Alto ahí Jurio!")