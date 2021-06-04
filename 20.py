#Ingresar como dato el perímetro de un cuadrado. Calcular e imprimir el volumen del cubo
#que tiene como lado el cuadrado antes mencionado.

perimetro = float(input("Ingresa el perimetro del cuadrado: "))

lado = perimetro / 4

base = lado * lado

volumen = base * lado

print(f"El volumen es {volumen}")

