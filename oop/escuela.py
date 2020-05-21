from random import randrange
# Una escuela tiene alumnos, cuyas características son:

# *Nombre
# *Apellido
# *Nota Matematica
# *Nota Lengua
# *Nota geografía
# *Promedio

# -Los alumnos pueden dar exámenes.

# La escuela también tiene profesores que tienen las siguientes características:

# *Nombre
# *Apellido
# *Materia que enseña

# -Los profesores toman exámenes y le dan al alumno una nota.

# Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y 
# que el resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Alumno(Persona):
    def __init__(self,nombre, apellido):
        self.notaMat = 0
        self.notaLeng = 0
        self.notaGeo = 0
        self.promedio = 0
        Persona.__init__(self, nombre, apellido)

    def obtener_promedio(self):
        promedio = (self.notaGeo + self.notaLeng + self.notaMat) / 3
        print(f"El promedio es: {promedio}")

    def hacer_examen(self, profesor):
        nota = profesor.tomar_examen()
        print(f"Haciendo el examen de {profesor.materia}...Recibiendo Nota....: {nota}")
        if profesor.materia == 'Geografia':
            self.notaGeo = nota
        if profesor.materia == 'Lengua':
            self.notaLeng = nota
        else:
            self.notaMat = nota
        self.obtener_promedio()

class Profesor(Persona):
    def __init__(self, materia, nombre, apellido):
        self.materia = materia
        Persona.__init__(self, nombre, apellido)

    def tomar_examen(self):
        nota = randrange(10)
        print(f"Tomando examen de {self.materia}.... Poniendo Nota....: {nota}")
        return nota



alumno1 = Alumno('Juan', 'Perez')

profesor1 = Profesor('Geografia', 'Carlos', 'Gallardo')
profesor2 = Profesor('Lengua', 'Lidia', 'Perez')
profesor3 = Profesor('Matematica', 'Pedro', 'Saenz')

print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Geografia la nota: {alumno1.notaGeo}")
print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Lengua la nota: {alumno1.notaLeng}")
print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Matematica la nota: {alumno1.notaMat}")

alumno1.hacer_examen(profesor1)
alumno1.hacer_examen(profesor2)
alumno1.hacer_examen(profesor3)

print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Geografia la nota: {alumno1.notaGeo}")
print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Lengua la nota: {alumno1.notaLeng}")
print(f"El Alumno {alumno1.nombre},{alumno1.apellido}, tiene en Matematica la nota: {alumno1.notaMat}")