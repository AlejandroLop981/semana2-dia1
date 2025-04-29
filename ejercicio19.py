numeros = []

for i in range (5) :
    numero = int (input (f"ingresa el numero que quieres agregar{i+1}: "))
    if numero % 2 == 0 :
        numeros.append(numero)

print ("lista actualizada", numeros)