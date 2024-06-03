#este programa sera utilizado para calcular el promedio de alumnos con porcentaje de act.

nombre = input("introduzca su nombre: ")
print("bienvenido " + nombre + " , este programa ayudará a calcular su calificacion final.")
print("""los porcentajes de evaluacion son:
tareas: 40%
proyectos: 40%
asistencia: 5%
exposicion: 15%""")
print()
tareas = int(input("introduzca el numero de tareas: "))
resultado_tareas = round(tareas * .40,2)
print()

tareas = int(input("introduzca el numero de proyectos: "))
resultado_proyectos = round(tareas * .40,2)
print()

tareas = int(input("introduzca el puntaje de su asistencia: "))
resultado_asistencia = round(tareas * .05,2)
print()

tareas = int(input("introduzca el puntaje de su exposición: "))
resultado_expo = round(tareas * .15,2)
print()

resultado_final = (resultado_tareas + resultado_proyectos + resultado_asistencia + resultado_expo)

print(nombre +" tu calificación final es de:", resultado_final)
