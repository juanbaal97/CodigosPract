#EJERCICIO WHILE CON BREAK VIDEO.24

print('while con la sentencia break')

contador = 0

while contador <10:
    contador += 1

    if contador ==5:
        break
    print('valor actual de la variable',contador)
print('FIN DEL PROGRAMA')


#EJERCICIO WHILE CON CONTINUE

print('while con la sentencia continue')

contador = 0

while contador <100:
    contador += 1

    if contador %2:
        continue 
    print('valor actual de la variable',contador)
print('FIN DEL PROGRAMA')
