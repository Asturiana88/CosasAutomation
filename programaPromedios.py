#Programa de promedios

#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado".
#Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

def promedioAlumno():
    nom = input("Ingrese Nombre del alumno: ")
    ape = input("Ingrese Apellido del alumno: ")
    mat = float(input("Ingrese Nota de Matemáticas del alumno: "))
    lit = float(input("Ingrese Nota de Literatura del alumno: "))
    fis = float(input("Ingrese Nota de Física del alumno: "))
    prom = (mat + lit + fis)/3

    if prom > 6:
        print("Aprobado")
        if prom >= 9:
            print("Alumno destacado")

    if prom < 4:
         print("Insuficiente")

    if prom >=4 and prom <= 5.99999:
        print("A recuperatorio")

#Distintas formas de concatenar:
    print("El alumno: " + nom + " " + ape + " tiene un promedio de: " + str(prom))
    print(f"El alumno: {nom} {ape} tiene un promedio de: {prom}")
    print("El alumno: {nom} {ape} tiene un promedio de: {prom}".format(nom=nom, ape=ape, prom=prom))
    print("El alumno: {0} {2} tiene un promedio de: {1}".format(nom, prom, ape))
    print("El alumno: {} {} tiene un promedio de: {:.2f}".format(nom, ape, prom))

promedioAlumno()