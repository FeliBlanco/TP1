#Ingresar un número por teclado e imprimir el valor absoluto del número.

numero = int(input("Ingrese un numero: "))

if(numero < 0):
    numero = numero * -1

print("El valor absoluto es: " + str(numero))