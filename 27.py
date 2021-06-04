#Leer dos números e imprimir el mayor, suponer que son distintos.

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

if(numero1 > numero2):
    print(f"El numero {numero1} es mayor que {numero2}")
elif(numero2 > numero1):
    print(f"El numero {numero2} es mayor que {numero1}")
else:
    print("Error: Los numeros no pueden ser iguales.")
