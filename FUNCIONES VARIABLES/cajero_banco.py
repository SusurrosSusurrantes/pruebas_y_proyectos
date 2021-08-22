usuarioEnBD="Neo"
claveEnBD="123456"
saldo=1000
#funciones

def validaUsuario(u, c):
  if u == usuarioEnBD and c == claveEnBD:
    return True
  return False


def login():
  usuario=input ("Ingrese su nombre de usuario: ")
  clave=input ("Ingrese su clave: ")
  return validaUsuario (usuario, clave)

def retirar(valor):
  if valor>saldo:
    return False, saldo
  return True, saldo-valor

def depositar(valor):
  return True, saldo + valor 

def accion(opcion):
  if opcion == 1:
    valor = int (input("Digite la cantidad a depositar "))
    return depositar(valor)

  if opcion == 2:
    valor = int (input("Ingrese el valor a retirar: "))
    return retirar(valor)

  return False, saldo

def ejecutar():
  if not login():
     return print ("Usuario o contraseña inválida")
    

  print("Qué deseas hacer?")
  opcion= int(input("1 Depositar o 2 Retirar "))

  ok, saldo = accion (opcion)
  if not ok:
     print ("No se realizó la acción, saldo: ", saldo)

  else:
     print("Acción realizada correctamente, saldo: ", saldo)

ejecutar()