from analizador_lexico import AnalizadorLexico

from analizador_sintactico import AnalizadorSintactico

from analizador_semantico import AnalizadorSemantico

from generador_codigo import GeneradorCodigo

codigo = """

inicio

a = 10;

b = 20;

c = a + b * 2;

si (c > 30) entonces

    escribir(c);

    d = c - 10;

finsi

escribir(d);

fin

"""

lexer = AnalizadorLexico(codigo)

tokens = lexer.tokenizar()

print("TOKENS:", tokens)


parser = AnalizadorSintactico(tokens)

ast = parser.analizar()



semantico = AnalizadorSemantico()

semantico.visitar(ast)

print("TABLA DE SÍMBOLOS:", semantico.tabla_simbolos)


print("\nCÓDIGO 3 DIRECCIONES:")

generador = GeneradorCodigo()

generador.generar(ast)