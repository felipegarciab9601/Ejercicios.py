#Listas con los ingredientes que se pueden añadir 
veg = ["Pimiento", "Tofu"]
no_veg = ["Peperoni", "Jamon", "Salmon"]


eleccion = str(input("Por favor selecciona tu pizza: vegetariana, o  no vegetariana:  "))
#Elaboracion de la pizza vegetariana
if eleccion == "vegetariana":
  print("Estos son los ingredientes de la vegetariana: " + str(veg))
  print("Escoge uno de los anteriores")
  escoge = str(int("Selecciona ingrediente: "))
  if escoge == "Pimiento":
    print("Los ingredientes son Mozarella, Tomate, {}".format(escoge))
  else:
    print("Los ingredientes son Mozarella, Tomate, Tofu")
else:
  print("Invalid")

#Elaboracion de la pzza no vegetariana
if eleccion == "no vegetariana":
  print("Estos son los ingredientes de la no vegetariana: " + str(no_veg))
  print("Escoge uno de los anteriores: ")
  escoge = str(input("Selecciona  el ingrediente: "))
  if escoge == "Peperoni":
    print("Tus ingredientes de Pizza son Mozarella, Tomate, Peperoni")
  elif escoge == "Jamon":
    print("Tus ingredientes de Pizza son Mozarella, Tomate, Jamon")  
  elif escoge == "Salmon":
    print("Tus ingredientes de Pizza son Mozarella, Tomate, Salmon")
  else:
    print("Comando no valido")  





