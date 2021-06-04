#Leer tres números distintos e imprimir el mayor

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

if(numero1 > numero2 and numero1 > numero3):
    print(f"El numero mayor es {numero1}")
elif(numero2 > numero1 and numero2 > numero3):
    print(f"El numero mayor es {numero2}")
elif(numero3 > numero1 and numero3 > numero2):
    print(f"El numero mayor es {numero3}")
else:
    print("Los numeros deben ser distintos.")