#Leer tres números y sumarlos, si la suma es mayor que 10, calcular la raíz cuadrada de la
#suma e imprimirla, de lo contrario, leer dos números más y sumarios junto a los primeros,
#luego imprimir la suma

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

suma = numero1 + numero2 + numero3

if(suma > 10):
    raiz = suma * suma
    print(f"La raiz cuadrada de la suma es: {raiz}")
else:
    numero4 = int(input("Ingrese otro numero: "))
    numero5 = int(input("Ingrese otro numero: "))
    suma = suma + numero4 + numero5
    print(f"La suma es: {suma}")