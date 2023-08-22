class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        totalasientos = 0
        for i in self.asientos:
            if type(i) == Asiento:
                totalasientos += 1
        return totalasientos
    
    def verificarIntegridad(self):
        original = True
        if self.registro != self.motor.registro:
            original = False
        else:
            for j in self.asientos:
                if type(j) == Asiento:
                        if j.registro != self.registro:
                            original = False
                            break

        if original:
            return "Auto original"        
        else:
            return "Las piezas no son originales"

        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, argumento):
        self.registro = argumento

    def asignarTipo(self, argumento):
        if argumento == "electrico" or argumento == "gasolina":
            self.tipo = argumento



    
