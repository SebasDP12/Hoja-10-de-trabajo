import re

TOKENS = [
    ("INICIO", r"INICIO\b"),
    ("FINSI", r"FINSI\b"),
    ("FIN", r"FIN\b"),
    ("SI", r"SI\b"),
    ("ENTONCES", r"ENTONCES\b"),
    ("ESCRIBIR", r"ESCRIBIR\b"),
    
    ("NUMERO", r"\d+"),
    ("IDENTIFICADOR", r"[a-zA-Z_]\w*"),
    
    ("MAS", r"\+"),
    ("MENOS", r"\-"),
    ("MULTI", r"\*"),
    ("DIV", r"/"),
    ("IGUAL", r"="),

    ("MAYOR", r">"),
    ("MENOR", r"<"),
    
    ("PUNTO_Y_COMA", r";"),
    ("PARI", r"\("),
    ("PARD", r"\)"),
    ("ESPACIO", r"[ \t\n]+"),
]

class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo

    def tokenizar(self):
        tokens = []
        while self.codigo:
            coincidencia = None
            for tipo, patron in TOKENS:
                regex = re.match(patron, self.codigo, re.IGNORECASE)
                if regex:
                    coincidencia = (tipo, regex.group(0))
                    if tipo != "ESPACIO":  
                        tokens.append(coincidencia)
                    self.codigo = self.codigo[len(coincidencia[1]):]
                    break
            if not coincidencia:
                raise SyntaxError(f"Token no reconocido: {self.codigo[0]}")
        return tokens
