print("***********************************")
print("programa para saber el numero mayor")
print("***********************************")

num_uno =(int(input("ingrese el primer número: ")))
num_dos =(int(input("ingrese el segundo número: ")))
num_tres =(int(input("ingrese el tercer número: ")))

if num_uno > num_dos and num_uno > num_tres:
    print("el número,", num_uno, "es el  mayor")
elif num_dos > num_tres and num_dos > num_uno:
    print("el número,", num_dos, "es el  mayor")
elif num_tres > num_uno and num_tres > num_dos:
    print("el número,", num_tres, "es el  mayor")
    
