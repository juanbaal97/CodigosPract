print("=======")
print("Conversor")
print("=======")

print("MENU DE OPCIONES:")
print("presione 1 para convertir de numero a palabra.")
print("presione 2 para convertir de palabra a numero.")

opcion = int(input("cuál es tu opcion? "))

if opcion == 1:
    print("conversor 'número a palabra'")

    opcion_uno = int(input("¿cuál es el número que deseas convertir? "))

    if opcion_uno == 1:
        print("el número es 'UNO'")
    elif opcion_uno == 2:
        print("el número es 'DOS'")
    elif opcion_uno == 3:
        print("el número es 'TRES'")
    elif opcion_uno == 4:
        print("el número es 'CUATRO'")
    elif opcion_uno == 5:
        print("el número es 'CINCO'")
    elif opcion_uno == 6:
        print("el número es 'SEIS'")
    elif opcion_uno == 7:
        print("el número es 'SIETE'")
    elif opcion_uno == 8:
        print("el número es 'OCHO'")
    elif opcion_uno == 9:
        print("el número es 'NUEVE'")
    elif opcion_uno == 10:
        print("el número es 'DIEZ'")
    else:
        print("el numero no se encuentra en el registro disponible")

elif opcion == 2:
    print("conversor 'palabra a número'")
    
    opcion_dos = str(input("¿cuál es el número que deseas convertir? "))
    opcion_dos = opcion_dos.lower()

    if opcion_dos == 'uno':
        print("el número es '1'")
    elif opcion_dos == 'dos':
        print("el número es '2'")
    elif opcion_dos == 'tres':
        print("el número es '3'")
    elif opcion_dos == 'cuatro':
        print("el número es '4'")
    elif opcion_dos == 'cinco':
        print("el número es '5'")
    elif opcion_dos == 'seis':
        print("el número es '6'")
    elif opcion_dos == 'siete':
        print("el número es '7'")
    elif opcion_dos == 'ocho':
        print("el número es '8'")
    elif opcion_dos == 'nueve':
        print("el número es '9'")
    elif opcion_dos == 'diez':
        print("el número es '10'")
else:
    print("el numero no se encuentra en el registro disponible")
                

