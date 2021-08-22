class arquero():
	def __init__(self, vida, damage, energia):
		self.vida=vida
		self.damage=damage
		self.energia=energia
		self.flecha_helada=False
		self.super_salto=False

	def flecha_helada(self):
		self.flecha_helada=True

	def super_salto(self):
		self.super_salto=True

	def estado(self):
		print ("Vida: ", self.vida, "\nDamage: ", self.damage, "\nEnergia: ", self.energia)


class yoimiya(arquero):
	hcucharita=""
	def cucharita(self):
		self.hcucharita="hace cucharita con vos ♥"

	def estado(self):
		print ("Vida: ", self.vida, "\nDamage: ", self.damage, "\nEnergia: ", 
			self.energia, "\n", self.hcucharita)

yoimiya=yoimiya(100,10,100)



yoimiya.cucharita()
yoimiya.estado()



