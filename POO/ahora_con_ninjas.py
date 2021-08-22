#Esta es la primera forma sin self

'''class NinjaPrincipal:
	hp=100
	resistencia=50
	xp=1
	vidas=3

	def game_over(self):
		print("Game Over")

ninja= NinjaPrincipal()
print(ninja.hp)

ninja_enemigo= NinjaPrincipal()
ninja_enemigo.hp=25
ninja_enemigo.resitencia=10
ninja_enemigo.vidas=1
print(ninja_enemigo.hp, ninja_enemigo.resitencia, ninja_enemigo.hp)'''

#Ahora con self

class NinjaPrincipal:
	def __init__(self, hp, resistencia, xp, vidas):
		self.hp=hp
		self.resistencia=resistencia
		self.xp=xp
		self.vidas=vidas

	def game_over(self):
		print("Game Over")

#Ahora creamos un objeto para verlo

ninja_enemigo = NinjaPrincipal(25,10,1,1)
ninja = NinjaPrincipal (100,50,1,3)

print(ninja_enemigo.resistencia)
