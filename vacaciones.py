print("===================================================================")
print("programa para mostrar los dias de vacaciones que merece un empleado")
print("===================================================================")

nombre = (input("ingrese su(s) nombre(s): "))
paterno = (input("ingrese su primer apellido: "))
materno = (input("ingrese su segundo apellido: "))
print("===================================================================")

area_trabajo = (int(input("ingrese su clave de trabajo: ")))

if area_trabajo == 1:
    print("===================================================================")
    antiguedad = (int(input("ingrese cuantos años ha trabajado en la empresa: ")))
    if antiguedad == 1 and antiguedad < 2:
        print ("usted tiene derecho a '7', (siete) dias de vacaciones.")
        print("===================================================================")
    elif antiguedad >= 2 and antiguedad <= 6:
        print ("usted tiene derecho a '14', (catorce) dias de vacaciones.")
        print("===================================================================")
    elif antiguedad >= 7 and antiguedad <= 100:
        print ("usted tiene derecho a '20', (veinte) dias de vacaciones.")
        print("===================================================================")
    else:
        print("¡Aun no tiene derecho a vacaciones!")

elif area_trabajo == 2:

        print("===================================================================")
        antiguedad = (int(input("ingrese cuantos años ha trabajado en la empresa: ")))
        if antiguedad == 1 and antiguedad < 2:
            print ("usted tiene derecho a '7', (siete) dias de vacaciones.")
            print("===================================================================")
        elif antiguedad >= 2 and antiguedad <= 6:
            print ("usted tiene derecho a '15', (quince) dias de vacaciones.")
            print("===================================================================")
        elif antiguedad >= 7 and antiguedad <= 100:
            print ("usted tiene derecho a '22', (veintidos) dias de vacaciones.")
            print("===================================================================")
        else:
            print("¡Aun no tiene derecho a vacaciones!")

elif area_trabajo == 3:

        print("===================================================================")
        antiguedad = (int(input("ingrese cuantos años ha trabajado en la empresa: ")))
        if antiguedad == 1 and antiguedad < 2:
            print ("usted tiene derecho a '10', (diez) dias de vacaciones.")
            print("===================================================================")
        elif antiguedad >= 2 and antiguedad <= 6:
            print ("usted tiene derecho a '20', (veinte) dias de vacaciones.")
            print("===================================================================")
        elif antiguedad >= 7 and antiguedad <= 100:
            print ("usted tiene derecho a '30', (treinta) dias de vacaciones.")
            print("===================================================================")
        else:
            print("¡Aun no tiene derecho a vacaciones!")

else:
    print("Area de trabajo inexistente.")
