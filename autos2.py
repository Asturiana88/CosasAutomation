# Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:
# 1-Ya no sabemos cuantos clientes tendremos,
# 2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
# 3-Lo mismo con la cantidad de puertas y los colores.
# 4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
# 5-Si la cantidad de clientes fue:
# --5.1: 0 a 5 personas no hay descuento
# --5.2: 6 a 10 personas: hay un descuento del 10%
# --5.3: 11 a 50 personas: hay un descuento del 15%
# --5.4: Más de 50 personas: El descuento es del 18%
# 6-Solo se va a mostrar que se vendió al final del programa

def obtener_precio_xMarca(marca):
    if marca == "ford":
        return 100000
    if marca == "chevrolet":
        return 120000
    if marca == "fiat":
        return 80000

def obtener_precio_xPuertas(puertas):
    if puertas == 2:
        return 50000
    if puertas == 4:
        return 65000
    if puertas == 5:
        return 78000

def obtener_precio_xColor(color):
    colores={
        "blanco": 10000,
        "azul":20000,
        "negro":30000
    }
    return colores[color]  


nextCustomer = True
cantClientes = 1
listaClientes = []

while nextCustomer == True:

    marcaok = False
    puertasok = False 
    colorok = False

    nombApe = input("Ingrese nombre y apellido: ")

    while marcaok == False:
        marca = input("Ingrese marca del auto; Ford, Chevrolet ó Fiat: ").lower()  
        if (marca == "fiat" or marca == "chevrolet" or marca == "ford"):
            marcaok = True
            break
        else:
            marcaok = False

    while puertasok == False:
        puertas = int(input("Ingrese cantidad de puertas; 2,4 ó 5: ").lower())
        if (puertas == 2 or puertas == 4 or puertas == 5):
            puertasok = True
            break
        else:
            puertasok = False

    while True:
        color = input("Ingrese color del auto; Blanco, Azul ó Negro: ").lower()
        if (color in ["blanco", "negro", "azul"]):
            break

    valorAutoMarca = obtener_precio_xMarca(marca)
    valorAutopuertas = obtener_precio_xPuertas(puertas)
    valorAutoColor = obtener_precio_xColor(color)

    print(f"Valores: {valorAutoMarca} ,{valorAutopuertas} ,{valorAutoColor}")    
    valorTotalAuto = (valorAutoMarca + valorAutopuertas + valorAutoColor)

    datosClientes = {
        'nombreyApellido': nombApe,
        'MarcaL': marca,
        'PuertasL': puertas,
        'ColorL': color,
        'valorTotalL': valorTotalAuto
    } 
    listaClientes.append(datosClientes.copy())
 
    print(f"Lista Clientes: {listaClientes}")
    print(f"Cantidad Clientes: {cantClientes}")
    #print(f"El Cliente: {nombApe}, compró un auto de la marca: {marca} valor: {valorAutoMarca}, con {puertas} puertas de un valor adicional de {valorAutopuertas} y de color {color}, con un adicional de {valorAutoColor}, pagando un total de {valorTotalAuto} ")
    
    continuar = input("Desea agregar un nuevo cliente? S/N: ").lower()
    cantClientes+=1

    if continuar == "s":
        nextCustomer = True
    elif continuar == "n":
        for cliente in listaClientes:
            print(f"El cliente {cliente['nombreyApellido']}, compro un auto marca {cliente['MarcaL']}, con cantidad de puertas {cliente['PuertasL']}, color: {cliente['ColorL']}")
            if cantClientes <= 5:
                print(f"No hay descuento, valor total: {cliente['valorTotalL']}")
            elif cantClientes <= 10:
                print(f"Descuento del 10%, valor total: {cliente['valorTotalL']*0.9}")
            elif cantClientes <= 50:
                print(f"Descuento del 15%, valor total: {cliente['valorTotalL']*0.85}")
            else:
                print(f"Descuento del 18%, valor total: {cliente['valorTotalL']*0.82}")
        nextCustomer = False

    