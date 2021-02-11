sino = 0

while sino != 1:
    x = "contraseña"
    pss = str( input("Introduce la contraseña: "))

    if pss.lower() != x :
        print("Contraseña incorrecta")
        print("")
        sino = 0
    else:
        print("Contraseña correcta")
        sino = 1
print("")

#Grupo A - Mujeres con nombre anterior a m - Hombres con nombre posterior a n
#Grupo B - Mujeres con nombre posterior a m - Hombres con nombre anterior a n

nom = str( input("¿Cuál es tu nombre?: "))
gen = str( input("¿Cuál es tu sexo? Ingresa H o M: "))

if (gen == "H" and gen == "h" and nom.lower() > "n") or (gen =="M" and gen =="m" and nom.lower() < "m"):
    print("Pertences al grupo A")
else:
    print("Perteneces al grupo B")