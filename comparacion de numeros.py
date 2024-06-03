print("introduce dos números a comparar:")

num_uno = int(input("introduce el primer número a comparar: "))
num_dos = int(input("introduce el segundo número a comparar: "))

print("los números a comparar son:", num_uno ," & ", num_dos)

if num_uno > num_dos:
    print("el numero mayor es:",num_uno)
if num_uno < num_dos:
    print("el numero mayor es:",num_dos)
if num_uno == num_dos:
    print(num_uno, " es igual a ", num_dos)
if num_uno != num_dos:
    print(num_uno, " es distinto de ", num_dos)
if num_uno <= num_dos:
    print("el numero",num_uno," es menor o igual que",num_dos)
if num_uno >= num_dos:
    print("el numero",num_uno ," es mayor o igual que",num_dos)
 
