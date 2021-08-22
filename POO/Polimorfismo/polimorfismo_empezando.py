class coche():
	def desplazamiento(self):
		print("Me desplazo usando 4 ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo usando 2 ruedas")

class camion():
	def desplazamiento(self):
		print("Me desplazo usando 6 ruedas")

#miVehiculo=moto()
#miVehiculo.desplazamiento()

#miVehiculo2=coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=camion()
#miVehiculo3.desplazamiento()

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=camion()
desplazamientoVehiculo(miVehiculo)