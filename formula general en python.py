#formula general

import math

print("este programa se realiza una operacion con la formula general  'la chicharronera'")
print()

def discriminante(a,b,c):
    discrim = pow(b,2) - (-4 * a * c)
    return discrim

def raices(a,b,disc):
    raiz_uno = (-b + math.sqrt(disc))/(2*a)
    raiz_dos = (-b - math.sqrt(disc))/(2*a)
    return raiz_uno, raiz_dos

print("calculo de raices")

a = int(input("ingrese el valor de A: "))
print()
b = int(input("ingrese el valor de B: "))
print()
c = int(input("ingrese el valor de C: "))

disc = discriminante(a,b,c)
print("los resultados son:", raices(a,b,disc))

