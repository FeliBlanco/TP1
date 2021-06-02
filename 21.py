km = int(input("Ingre los KM recorridos: "))
precioCombustible = int(input("Ingresa el precio del combustible por litro: "))
kmPorLitro = int(input("Ingresa los KM recorridos por litro: "))

litroConsumido = km / kmPorLitro
gastoCombustible = litroConsumido * precioCombustible

print("Litros consumidos: "+str(litroConsumido))
print("Se gasto $"+str(gastoCombustible)+" en combustible.")