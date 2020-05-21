class Automovil():
    def __init__(self, color,marca,velocidad_max):
        self.color = color
        self.marca = marca
        self.velocidad_max = velocidad_max
        self.velox_actual = 0
    def mostrar_velocimetro(self):
        print(f"La velocidad actual es de {self.velox_actual} de {self.velocidad_max}")
    def acelerar(self, velocidad):
        self.velox_actual = self.velox_actual + velocidad
    def frenar(self, velocidad):
        self.velox_actual = self.velox_actual - velocidad

mi_auto = Automovil('verde','fiat',180)
print(mi_auto.color)
mi_auto.mostrar_velocimetro()