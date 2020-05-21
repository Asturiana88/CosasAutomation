class Vehiculo():
    def __init__(self, color,marca,velocidad_max):
        self.color = color
        self.marca = marca
        self.velocidad_max = velocidad_max
        self.velox_actual = 0
        self.encendido = False

    def encender_vehiculo(self):
        self.encendido = True
        print("Auto encendido")

    def apagar_vehiculo(self):
        self.encendido = False
        print("Auto Apagado")

    def mostrar_velocimetro(self):
        print(f"La velocidad actual es de {self.velox_actual} de {self.velocidad_max}")
    
    def acelerar(self, velocidad):
        if self.encendido:
            if self.velox_actual + velocidad >= self.velocidad_max:
                self.velox_actual = self.velocidad_max
            else:
                self.velox_actual = self.velox_actual + velocidad
            self.mostrar_velocimetro()
        else:
            print("Encender el auto primero")
    
    def frenar(self, velocidad):
        if self.encendido:
            if self.velox_actual - velocidad <=0:
                self.velox_actual = 0
            else:
                self.velox_actual = self.velox_actual - velocidad
            self.mostrar_velocimetro()
        else:
            print("Encender el auto primero")



class Automovil(Vehiculo):
    def __init__(self, cantRuedas, color, marca, velocidad_max):
        self.cantRuedas = cantRuedas
        Vehiculo.__init__(self, color, marca,velocidad_max)

    def abrir_puertas(self, nroPuertas):
        print(f"Se abrieron {nroPuertas} puertas")
    
    def mostrar_velocimetro(self):
        print(f"La velocidad actual del Auto es de {self.velox_actual} de {self.velocidad_max}")

class Camion(Vehiculo):
    def __init__(self, cargaMax, color, marca, velocidad_max):
        self.cargaMax = cargaMax
        self.cargaInicial = 0
        Vehiculo.__init__(self, color, marca, velocidad_max)

    def cargar(self, carga):
        self.cargaInicial = self.cargaInicial + carga
        
    def mostrar_velocimetro(self):
        print(f"La velocidad actual del Camion es des {self.velox_actual} de {self.velocidad_max}")

    

mi_auto = Automovil(4,'Verde', 'Fiat', 190)
mi_auto.encender_vehiculo()
mi_auto.acelerar(220)
mi_auto.apagar_vehiculo()
mi_auto.frenar(5000)
mi_auto.abrir_puertas(2)
mi_auto.mostrar_velocimetro()


mi_camion = Camion(1000, 'Rojo', 'Ford', 90)
mi_camion.cargar(10000)
mi_camion.mostrar_velocimetro()