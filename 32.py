#. Se leen el sueldo básico y la categoría de un empleado. Para calcular el sueldo neto se
#efectúan los siguientes descuentos:
#Categoría 1: 30%
#Categoría 2: 25%
#Categoría 3: 25%
#Categoría 4: 1 0%
#Para otras Categorías no hay descuentos. Imprimir el sueldo neto básico y Categoría.

sueldo = float(input("Ingresa el sueldo: "))
categoria = int(input("Ingresa la categoria: "))

if(categoria == 1):
    sueldo = sueldo - ((sueldo * 30) / 100)
elif(categoria == 2 or categoria == 3):
    sueldo = sueldo - ((sueldo * 25) / 100)
elif(categoria == 4):
    sueldo = sueldo - ((sueldo * 10) / 100)    

print(f"Categoria: {categoria} - Sueldo neto: {sueldo}")