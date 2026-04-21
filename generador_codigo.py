class GeneradorCodigo:
    def __init__(self):
        self.contador_temporales = 0

    def nuevo_temporal(self):
        self.contador_temporales += 1
        return f"t{self.contador_temporales}"

    def generar(self, nodo):
        metodo = getattr(self, f"gen_{type(nodo).__name__}")
        return metodo(nodo)

    def gen_Programa(self, nodo):
        for sentencia in nodo.sentencias:
            self.generar(sentencia)

    def gen_Asignacion(self, nodo):
        valor = self.generar(nodo.valor)
        print(f"{nodo.nombre} = {valor}")

    def gen_Imprimir(self, nodo):
        valor = self.generar(nodo.valor)
        print(f"escribir {valor}")

    def gen_Si(self, nodo):
        condicion = self.generar(nodo.condicion)
        etiqueta = "L1"
        print(f"if_false {condicion} goto {etiqueta}")
        for sentencia in nodo.cuerpo:
            self.generar(sentencia)
        print(f"{etiqueta}:")

    def gen_OperacionBinaria(self, nodo):
        izq = self.generar(nodo.izquierda)
        der = self.generar(nodo.derecha)
        temp = self.nuevo_temporal()
        print(f"{temp} = {izq} {nodo.operador} {der}")
        return temp

    def gen_Numero(self, nodo):
        return str(nodo.valor)

    def gen_Variable(self, nodo):
        return nodo.nombre
