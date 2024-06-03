print("====================")
print("operadores logicos")
print("====================")

num_uno = int(input("introduce el valor para la variable num_uno: "))

if num_uno >= 5 and num_uno <=10:
    print ("el valor de la variable cumple la condición.")
else:
    print("el valor de la variable no cumplio la condición")
    

palabra =str(input("escribe 'SI' ó 'YES': "))

if palabra == "SI" or palabra == "YES":
    print ("la variable SI cumple la condición.")
else:
    print("la variable NO cumplio la condición")

num_dos =int(input("introduce un numero igual a 10: "))

if not num_uno ==10 :
    print("SI cumple la condición. ")
else:
    print("NO cumple la condicion")

print("ADIOS!")
