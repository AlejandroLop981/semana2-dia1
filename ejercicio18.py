numeros = [10, 20, 30, 40, 50]
print (numeros)

num = int (input("ingresa un numero: "))
posicion = int (input("elige la posicion (del 1 al 4): "))
numeros.insert(posicion, num)

print ("lista actualizada")
print (numeros)