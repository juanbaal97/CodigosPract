nombre = "CarloS gallardo"

print(nombre.istitle())

nombre = nombre.title()
print(nombre)
print(nombre.istitle())



nombre = str(input('nombre: '))
nombre_dos = str(input('segundo nombre: '))
apellido = str(input('apellido: '))
edad = str(input('edad:'))

completo = (f"{nombre} {nombre_dos} {apellido}, tienes una edad de {edad} años")

print(f'el formato istitle(), se ha aplicado?: {completo.istitle()}')
print(f'el formato title(), se ha aplicado?: {completo.title()}')

