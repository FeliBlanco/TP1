#. Leer un número comprendido entre uno y siete, ambos inclusive e imprimir el nombre del
#día de la semana correspondiente

numero = int(input("Ingrese un numero: "))
if(numero == 1):
    print("Domingo")
elif(numero == 2):
    print("Lunes")
elif(numero == 3):
    print("Martes")
elif(numero == 4):
    print("Miercoles")  
elif(numero == 5):
    print("Jueves")
elif(numero == 6):
    print("Viernes")
elif(numero == 7):
    print("Sabado")
else:
    print("Ingresa un numero entre uno y siete.")