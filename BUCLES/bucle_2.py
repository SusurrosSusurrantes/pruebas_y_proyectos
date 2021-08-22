email=False
miEmail=input("Introduce tu correo electrónico: ")

for i in miEmail:
	if(i=="@"):
		email=True

if email==True:
	print("Adelante maquinola")

else:
	print("Eso no es un email papu ¬¬")