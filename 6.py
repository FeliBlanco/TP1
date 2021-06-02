altura = int(input("Ingrese la altura de la pared: "))
largo = int(input("Ingrede el largo de la pared: "))

pinturaPorMetro = 3.6

metrosc = largo * altura

pintura = metrosc / 3.6

pintura = pintura / 2

print("Se necesitaran " + str(pintura) + " litros de pintura")