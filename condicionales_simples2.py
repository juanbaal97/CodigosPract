#video numero. 10

print ("sistema para calcular el promedio de un alumnno.")

nombre = str(input("¿cúal es tu nombre? "))
apellido = str(input("¿cúal es tu primer apeliido? "))
segundo_apellido = str(input("¿cúal es tu segundo apeliido? "))
grupo = int(input("¿en que semestre estudias actualmente? "))

if grupo == 1:
    print("""Tu tira de materias es:
          Matemáticas.
          física.
          español.
          introduccion a la ingenieria.
          algoritmos.
          contabilidad.""")
    
    mate = int(input("introduce la calificacion de tu materia en matemáticas:"))
    fisica = int(input("introduce la calificacion de tu materia en física:"))
    espanol = int(input("introduce la calificacion de tu materia en español:"))
    introd = int(input("introduce la calificacion de tu materia en introduccion a la ingenieria:"))
    algo = int(input("introduce la calificacion de tu materia en algoritmos:"))
    conta = int(input("introduce la calificacion de tu materia en contabilidad:"))

    resultado = round((mate + fisica + espanol + introd + algo + conta)/6,1)

    if resultado > 6:
        print("Felicidades! " + nombre + " " + apellido + " " + segundo_apellido + " Tu promedio final del semestre es de: ",resultado)
        print("nos vemos en el segundo semestre. :)")
    else:
        print("No aprobaste el semestre! " + nombre + apellido +  segundo_apellido + " Tu promedio final del semestre es de: ",resultado)

        
if grupo == 2:
        print("""Tu tira de materias es:
          Matemáticas II.
          física II.
          derecho.
          introduccion a la computación.
          programación.
          diseño de sistemas básicos.""")
        
        mate = int(input("introduce la calificacion de tu materia en matemáticas:"))
        fisica = int(input("introduce la calificacion de tu materia en física:"))
        derecho = int(input("introduce la calificacion de tu materia en derecho:"))
        intro_com = int(input("introduce la calificacion de tu materia en introduccion a la computación:"))
        programacion = int(input("introduce la calificacion de tu materia en programación:"))
        diseño = int(input("introduce la calificacion de tu materia en diseño de sistemas básicos:"))

        resultado = round((mate + fisica + derecho + intro_com + programacion + diseño)/6,1)

        if resultado > 6:

            print("Felicidades! " + nombre + " " + apellido + " " + segundo_apellido + " Tu promedio final del semestre es de: ",resultado)
            print("nos vemos en el tercer semestre. :)")
        else:

            print("No aprobaste el semestre! " + nombre + apellido +  segundo_apellido + " Tu promedio final del semestre es de: ",resultado)
        
    
