from nodes import *

class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def consumir(self, tipo):
        token = self.actual()
        if token and token[0] == tipo:
            self.pos += 1
            return token[1]
        raise SyntaxError(f"Se esperaba {tipo} pero se encontró {token}")
    
    def analizar(self):
        self.consumir("INICIO")
        sentencias = []
        while self.actual() and self.actual()[0] != "FIN":
            sentencias.append(self.sentencia())
        self.consumir("FIN")
        return Programa(sentencias)
    
    def sentencia(self):
        token = self.actual()
        if token[0] == "IDENTIFICADOR":
            return self.asignacion()
        elif token[0] == "ESCRIBIR":
            return self.imprimir()
        elif token[0] == "SI":
            return self.si()
        else:
            raise SyntaxError(f"Sentencia no válida con token: {token}")
    
    def asignacion(self):
        nombre = self.consumir("IDENTIFICADOR")
        self.consumir("IGUAL")
        valor = self.expresiones()
        self.consumir("PUNTO_Y_COMA")
        return Asignacion(nombre, valor)
    
    def imprimir(self):
        self.consumir("ESCRIBIR")
        self.consumir("PARI")
        valor = self.expresiones()
        self.consumir("PARD")
        self.consumir("PUNTO_Y_COMA")
        return Imprimir(valor)
    
    def si(self):
        self.consumir("SI")
        self.consumir("PARI")
        condicion = self.comparacion() 
        self.consumir("PARD")
        self.consumir("ENTONCES")
        cuerpo = []
        while self.actual() and self.actual()[0] != "FINSI":
            cuerpo.append(self.sentencia())
        self.consumir("FINSI")
        return Si(condicion, cuerpo)

    def comparacion(self):
        izquierda = self.expresiones()
        while self.actual() and self.actual()[0] in ("MAYOR", "MENOR"):
            operador = self.consumir(self.actual()[0])
            derecha = self.expresiones()
            izquierda = OperacionBinaria(izquierda, operador, derecha)
        return izquierda
    
    def expresiones(self):
        izquierda = self.termino()
        while self.actual() and self.actual()[0] in ("MAS", "MENOS"):
            operador = self.consumir(self.actual()[0])
            derecha = self.termino()
            izquierda = OperacionBinaria(izquierda, operador, derecha)
        return izquierda

    def termino(self):
        izquierda = self.factor()
        while self.actual() and self.actual()[0] in ("MULTI", "DIV"):
            operador = self.consumir(self.actual()[0])
            derecha = self.factor()
            izquierda = OperacionBinaria(izquierda, operador, derecha)
        return izquierda

    def factor(self):
        token = self.actual()
        if token[0] == "NUMERO":
            return Numero(int(self.consumir("NUMERO")))
        elif token[0] == "IDENTIFICADOR":
            return Variable(self.consumir("IDENTIFICADOR"))
        elif token[0] == "PARI":
            self.consumir("PARI")
            nodo = self.expresiones()
            self.consumir("PARD")
            return nodo
        raise SyntaxError(f"Se esperaba un número, variable o paréntesis pero se encontró {token}")
