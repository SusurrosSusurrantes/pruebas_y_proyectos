import turtle

#ventana
wn=turtle.Screen()
wn.tittle("Pong, traspaso de código")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#JugadorA
JugadorA=turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("white")
JugadorA.penup()
JugadorA.goto(-350,0)

while True:
	wn.update()
