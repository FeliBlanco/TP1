#Leer tres números, calcular e imprimir los seis posibles cocientes

numero = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

cociente1 = numero / numero2
cociente2 = numero2 / numero
cociente3 = numero3 / numero
cociente4 = numero / numero3
cociente5 = numero2 / numero3
cociente6 = numero3 / numero2

print("Posibles cocientes: ")
print(str(cociente1) + " - " + str(cociente2) + " - " + str(cociente3) + " - " + str(cociente4) + " - " + str(cociente5) + " - " + str(cociente6))