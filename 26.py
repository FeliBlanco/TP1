#Leer tres números, si el segundo es negativo, calcular la raíz cuadrada de la suma de los
#restantes; en caso contrario imprimir un mensaje de error

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
numero3 = int(input("Ingresa otro numero: "))

if(numero2 < 0):
    suma = numero1 + numero3
    raiz = suma * suma
    #en el enunciado no dice imprimir el resultado :p pero por las dudas
    print(f"La raiz cuadrada es: {raiz}")
else:
    print("Error: El segundo numero no es negativo.")