#Si un lote de terreno tiene X metros de frente por Y metros de fondo: calcular e imprimir la
#cantidad da metros de alambre para cercarlo. (X e Y serán leídos al comenzar el programa).


frente = int(input("Ingrese los metros del frente: "))
fondo = int(input("Ingrede los metros del fondo: "))

alambre = (frente * 2) + (fondo * 2)

print("Se necesitaran " + str(alambre) + " metros de alambre.")