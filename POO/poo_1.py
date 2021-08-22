#Creamos una clase
class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	def arrancar(self):
		self.enMarcha=arrancamos
		if (self.enMarcha):
			return "el coche está en marcha"

		else:
			return "el coche está parado"
		self.enMarcha=True

	def estado(self):
		print("El coche tiene ", self.ruedas, "un ancho de ",
		self.anchoChasis, "y un largo de ", self.largoChasis)

#Instanciamos una clase, es tu primer objeto
miCoche=Coche()
#nomenclatura del punto
print(miCoche.largoChasis)
miCoche.arrancar(True)
print(miCoche.estado())

#otro objeto
print("---Ahora viene otro objeto---")

miCoche2=Coche()
print("El largo del coche es ", miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, "ruedas")
miCoche2.arrancar(False)
print(miCoche2.estado())