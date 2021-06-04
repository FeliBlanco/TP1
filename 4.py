#Teniendo como dato el lado de un cuadrado, calcular e imprimir la superficie y perímetro.


lado = int(input("Ingresa un lado del cuadrado: "))

perimetro = lado * 4
superficie = lado * lado

print("Perimetro: " + str(perimetro) + " - Superficie: " + str(superficie))