class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = {}

    def visitar(self, nodo):
        metodo = getattr(self, f"visitar_{type(nodo).__name__}")
        return metodo(nodo)

    def visitar_Programa(self, nodo):
        for sentencia in nodo.sentencias:
            self.visitar(sentencia)

    def visitar_Asignacion(self, nodo):
        valor = self.visitar(nodo.valor)
        self.tabla_simbolos[nodo.nombre] = valor

    def visitar_Imprimir(self, nodo):
        valor = self.visitar(nodo.valor)
        return valor

    def visitar_Si(self, nodo):
        condicion = self.visitar(nodo.condicion)
        if condicion:
            for sentencia in nodo.cuerpo:
                self.visitar(sentencia)

    def visitar_OperacionBinaria(self, nodo):
        izq = self.visitar(nodo.izquierda)
        der = self.visitar(nodo.derecha)

        if nodo.operador == "+": return izq + der
        elif nodo.operador == "-": return izq - der
        elif nodo.operador == "*": return izq * der
        elif nodo.operador == "/": return izq // der
        elif nodo.operador == ">": return izq > der
        elif nodo.operador == "<": return izq < der

    def visitar_Numero(self, nodo):
        return nodo.valor

    def visitar_Variable(self, nodo):
        if nodo.nombre not in self.tabla_simbolos:
            raise Exception(f"Variable no definida: {nodo.nombre}")
        return self.tabla_simbolos[nodo.nombre]
