class Nodo:
    pass

class Programa(Nodo):
    def __init__(self, sentencias):
        self.sentencias = sentencias

class Asignacion(Nodo):
    def __init__(self, nombre, valor):
        super().__init__()
        self.nombre = nombre
        self.valor = valor

class Imprimir(Nodo):
    def __init__(self, valor):
        self.valor = valor

class Si(Nodo):
    def __init__(self, condicion, cuerpo):
        self.condicion = condicion
        self.cuerpo = cuerpo

class OperacionBinaria(Nodo):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

class Numero(Nodo):
    def __init__(self, valor):
        self.valor = valor

class Variable(Nodo):
    def __init__(self, nombre):
        self.nombre = nombre
