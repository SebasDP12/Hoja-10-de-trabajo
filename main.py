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

if __name__ == "__main__":
    print("--- 1. LEXER ---")
    lexer = AnalizadorLexico(codigo)
    tokens = lexer.tokenizar()
    print("TOKENS:", tokens)

    print("\n--- 2. PARSER ---")
    parser = AnalizadorSintactico(tokens)
    ast = parser.analizar()
    print("AST construido con éxito.")

    print("\n--- 3. SEMÁNTICO ---")
    semantico = AnalizadorSemantico()
    semantico.visitar(ast)
    print("TABLA DE SÍMBOLOS:", semantico.tabla_simbolos)

    print("\n--- 4. CÓDIGO 3 DIRECCIONES ---")
    generador = GeneradorCodigo()
    generador.generar(ast)
