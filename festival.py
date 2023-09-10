print ("***Festival musical***")
print ("*****")
print ("0. Salir")
print ("1. Registrar bandas")
print ("2. Mostrar bandas que no se han presentado")
print ("3. Cambiar la hora de presentacion")
print ("4. Retirar una agrupacion")
print ("5. Mostrar Todas la bandas")
print ("******")

opcion=90
bandas=[]

while (opcion != 0):
  grupo={}
  
  opcion=int(input("Digita una opcion: "))
  if opcion == 1:
    grupo["nombre"] = input("ingrese el nombre de la banda: ")
    grupo["id"] = int(input("Ingrese un id: "))
    grupo["genero"] = input("Ingrese el genero: ")
    grupo["hora"] =  input ("Ingrese la hora de presentacion: ")
    grupo["pago"] = float(input("Ingrese el pago de la banda: "))
    grupo["estado"] = int(input("Ya te presentaste, si es si ingresa 1, sino ingresa 0: "))
    bandas.append(grupo)
  elif opcion==2 :
    for banda in bandas: 
      if(banda['estado'] == 0):
        print (banda)
  elif opcion == 3:
     for banda in bandas: 
      if(banda['estado'] == 0):
        banda['hora'] = input("Ingrese la nueva hora de presentacion: ")
  elif opcion == 4:
    for banda in bandas: 
        if(banda['estado'] == 0):
            print ("******")
            print(banda)
    eliminar = int(input("Ingrese el Id de la banda a eliminar: "))
    for banda in bandas: 
        if banda['id'] == eliminar:
            bandas.remove(banda) 
            print("Banda Retirada Exitosamente")   
  elif opcion==5 :
    for banda in bandas: 
        print (banda)