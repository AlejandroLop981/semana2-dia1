lista = ["Samuel", "Mateo", "Alejo", "Mateo", "Samuel", "Samuel"]
print (lista)
nbuscado = input ("introduce un nombre de la lista para contar: ")
cantidad = lista.count(nbuscado)

print (f"el nombre {nbuscado} se repite {cantidad} veces")