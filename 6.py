#Un pintor sabe que con una pintura determinada puede pintar 3,6 metros cuadrados por cada
#medio litro. Sabiendo la altura y el largo de la pared a pintar, informar cuántos litros de
#pintura utilizará. (Altura y Largo en metros)

altura = int(input("Ingrese la altura de la pared: "))
largo = int(input("Ingrede el largo de la pared: "))

pinturaPorMetro = 3.6

metrosc = largo * altura

pintura = metrosc / 3.6

pintura = pintura / 2

print("Se necesitaran " + str(pintura) + " litros de pintura")