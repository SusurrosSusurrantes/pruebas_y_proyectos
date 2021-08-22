Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5+6
11
>>> 10%3
1
>>> 5**3
125
>>> 9/2
4.5
>>> 9%2
1
>>> 9//2
4
>>> nombre=5
>>> type(nombre)
<class 'int'>
>>> nombre="Juan"
>>> type(nombre)
<class 'str'>
>>> nombre=5,2
>>> type(nombre)
<class 'tuple'>
>>> mensaje="""Esto es un mensaje
... con tres saltos
... de línea"""print(mensaje)
  File "<stdin>", line 3
    mensaje="""Esto es un mensaje
con tres saltos
de línea"""print(mensaje)
                ^
SyntaxError: invalid syntax
>>> mensaje="""Esto es un mensaje
... con tres saltos
... de línea"""
>>> print(mensaje)
Esto es un mensaje
con tres saltos
de línea
>>> numero1=5
>>> numero2=7
>>> if numero1>numero2:
... 	print("el numero 1 es mayor")
... else:
... 	print("el numero 2 es mayor")
... 
el numero 2 es mayor
>>> print("Aguante Perón")