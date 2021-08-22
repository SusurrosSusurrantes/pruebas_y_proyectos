#print("Ingresa tu correo: ")

#correo=input()

#def correoVer():
#	if (correo=="@" and "","@" !="@","@"):
#		print("Tu correo es correcto")

#	else:
#		print("Correo incorrecto")

#Ahora bien hecho:
mailUsuario=input("Introduce tu dirección de email: ")
arroba=mailUsuario.count("@")

if (arroba != 1 or mailUsuario.rfind("@")==(len(mailUsuario) -1) or mailUsuario.find("@")==0):
	print("Correo incorrecto")

else:
	print("Correo correcto")

