#Teniendo como dato el tiempo transcurrido desde el inicio hasta el final de un
#acontecimiento cualquiera expresado en días, hacer los cálculos necesarios e imprimirlo en
#MINUTOS

dias = int(input("Ingresa los dias transcurridos: "))

horas = dias * 24
minutos = horas * 60

print(f"Transcurrió {minutos} minutos.")