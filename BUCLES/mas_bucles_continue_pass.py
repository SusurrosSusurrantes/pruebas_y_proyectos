email=input("Introduce tu email porfavor: ")
for i in email:

	if i=="@":
		arroba=True
		break;

else:

	arroba=False

print (arroba)