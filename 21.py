#Ingresar por teclado los precios correspondientes a cinco artículos y las cantidades vendidas
#de cada uno de ellos. Calcular e imprimir el importe total de ventas de cada uno y un importe
#total de lo vendido.

km = int(input("Ingre los KM recorridos: "))
precioCombustible = int(input("Ingresa el precio del combustible por litro: "))
kmPorLitro = int(input("Ingresa los KM recorridos por litro: "))

litroConsumido = km / kmPorLitro
gastoCombustible = litroConsumido * precioCombustible

print("Litros consumidos: "+str(litroConsumido))
print("Se gasto $"+str(gastoCombustible)+" en combustible.")