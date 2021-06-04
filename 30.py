#En un comercio se venden tres modelos de frascos codificados uno, dos y tres. Ingresando un
#código, se quiere imprimir la descripción según detalle:
#1 -chico. 2- mediano. 3- grande.

codigo = int(input("Ingresa el codigo: "))
if(codigo == 1):
    print("Descripción: chico.")
elif(codigo == 2):
    print("Descripción: mediano.")    
elif(codigo == 3):
    print("Descripción: grande.")   
else:
    print("Codigo invalido.")