#Dado un número entero positivo menor que cien, lerdo desde teclado, indicar si es primo. 

while(True):
    numero = int(input("Ingresa un numero: "))
    if(numero < 100 and numero > 0):
        if(numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0):
            print("El numero no es primo.")
            break
        else:
            print("El numero es primo.")
            break
    else:
        print("Ingresa un numero menor que 100 y positivo.")