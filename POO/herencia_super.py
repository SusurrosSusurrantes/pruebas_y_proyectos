class Persona():
	def __init__(self, nombre, edad, lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

#super() llama a las funciones de la clase padre
class Empleado(Persona):
	def __init__(self, salario, antigüedad):
		super().__init__("Antonio",55,"España")

		self.salario=salario
		self.antigüedad=antigüedad

Antonio=Empleado(1500,15)
Antonio.descripcion()
#Esto te sirve para conocer a qué clase pertenece cada subclase
isinstance(Antonio, Empleado)
print(isinstance(Antonio,Empleado))