edad = int (input ("introduce tu edad"))

if edad < 13 :
    print ("eres un niño")
elif edad >= 13 and edad < 18 :
    print ("eres un adolescente")
if edad >= 18 and edad < 60 :
    print ("eres un adulto")
else :
    print ("eres un anciano")