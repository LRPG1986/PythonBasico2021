x = int( input("Introduce la altura del triangulo: "))

for i in range(x):
    print("")
    for j in range(i+1):
        print("*", end="")
print("\n")

y = int( input("Introduce un número: "))
print("")

if y%2==0:
    print(str(y) + " no es un número primo")
else:
    print(str(y) + " es un número primo")