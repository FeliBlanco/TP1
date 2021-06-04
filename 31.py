#Leer tres números, si el primero es uno, sumar el segundo y el tercero; si es dos.
#multiplicarlos, si es tres, dividirlos, si es cuatro, la raíz cuadrada de la suma de sus cuadrados
#y cualquier otro valor indicar que se trata de un error.

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

resultado = 0

if(numero1 == 1):
    resultado = numero2 + numero3
elif(numero1 == 2):
    resultado = numero2 * numero3
elif(numero1 == 3):
    resultado = numero2 / numero3
elif(numero1 == 4):
    resultado = (numero2 * numero2) + (numero3 * numero3)
    resultado = resultado * resultado
else:
    print("Error: El primer numero tiene un desconocido.")

if(resultado != 0):
    print(f"El resultado es: {resultado}")