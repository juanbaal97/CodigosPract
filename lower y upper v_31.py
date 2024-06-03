string = input('Introduce una cadena: ')

print(f"¿Todos los caracteres estan en minusculas?: {string.islower()}")
string = string.lower()
print(f"string en minúsculas: {string}")


string_dos = input('Introduce una cadena: ')
string_dos
print(f"¿Todos los caracteres estan en mayúsculas?: {string.isupper()}")
string_dos = string_dos.upper()
print(f"string en mayúsculas: {string_dos}")
