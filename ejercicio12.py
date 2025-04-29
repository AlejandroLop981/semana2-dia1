frutas = ["manzana", "platano", "arroz"]

print ("lista de frutas:", (frutas))
eliminar = input ("que fruta deseas eliminar?: ")

if eliminar in frutas :
    frutas.remove(eliminar)
else :
    print ("la fruta no está en la lista")

print ("lista actualizada,", (frutas))