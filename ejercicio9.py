nota = int (input ("ingresa tu calificacion: "))

if nota < 5 :
    print ("reprobaste")
elif nota >= 5 and nota < 7 :
    print ("aprobaste")
if nota >= 7 and nota <= 10 :
    print ("sobresaliente")
else :
    print ("nota invalida")