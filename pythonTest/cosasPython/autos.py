#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#*Nombre y apellido del comprador.
#*Marca
#*Puertas
#*Color
#Marcas posibles y sus precios:
#-Ford $100000
#-Chevrolet: $120000
#-Fiat: $80000
#-Por la cantidad de puertas se añade un precio:
#-2: $50000
#-4: $65000
#-5: $78000
#Dependiendo del color, se deben sumar:
#-Blanco: $10000
#-Azul: $20000
#-Negro: $30000
#Deben imprimirse los datos de cada compra y el precio total.

def obtener_precio_xMarca(marca):
    if marca == "Ford".lower():
        return 100000
    if marca == "Chevrolet".lower():
        return 120000
    if marca == "Fiat".lower():
        return 80000

def obtener_precio_xPuertas(puertas):
    if puertas == 2:
        return 50000
    if puertas == 4:
        return 65000
    if puertas == 5:
        return 78000

def obtener_precio_xColor(color):
    if color == "Blanco".lower():
        return 10000
    if color == "Azul".lower():
        return 20000
    if color == "Negro".lower():
        return 30000    


CANT_CLIENTES = 5

for _ in range(0, CANT_CLIENTES-1):
    nombApe = input("Ingrese nombre y apellido: ")
    marca = input("Ingrese marca del auto; Ford, Chevrolet ó Fiat: ").lower()
    puertas = int(input("Ingrese cantidad de puertas; 2,4 ó 5: ").lower())
    color = input("Ingrese color del auto; Blanco, Azul ó Negro ").lower()

    valorAutoMarca = obtener_precio_xMarca(marca)
    valorAutopuertas = obtener_precio_xPuertas(puertas)
    valorAutoColor = obtener_precio_xColor(color)

    valorTotalAuto = valorAutoMarca + valorAutopuertas + valorAutoColor

    print(f"El Cliente: {nombApe}, compró un auto de la marca: {marca} valor: {valorAutoMarca}, con {puertas} puertas de un valor adicional de {valorAutopuertas} y de color {color}, con un adicional de {valorAutoColor}, pagando un total de {valorTotalAuto} ")
