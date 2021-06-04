#Leer dos números reales, calcular e imprimir los dos posibles cocientes entre ellos

numero = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

cociente1 = numero / numero2
cociente2 = numero2 / numero

print("Posibles cocientes: ")
print(str(cociente1) + " - " + str(cociente2))