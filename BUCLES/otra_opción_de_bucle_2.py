contador=0
miEmail=input("Introduce tu Email: ")
for i in miEmail:
	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:
	print("Adelante Maquinola")

else:
	print("Adónde crees que vas ¬¬")
