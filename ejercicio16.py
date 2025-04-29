lista = [4, 5, 6, 1, 2, 8, 12]

buscar = int (input ("introduce un numero para buscar: "))

if buscar in lista :
    posicion = lista.index(buscar)
    print (f"tu numero está en la posicion {posicion} ")
else :
    print ("el numero no se encuentra en la lista")