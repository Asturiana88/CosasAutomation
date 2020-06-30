#Sin funcion
arrayNumeros = [1,3,2,7,8,5,100,45,28,4,6]
arrayNumeros.sort()
print(arrayNumeros)

#Con funcion
def organizarArray(arrayElem):
    arrayNumeros.sort()
    return arrayElem.sort()

organizarArray(arrayNumeros)