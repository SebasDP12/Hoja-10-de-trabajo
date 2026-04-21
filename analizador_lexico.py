import re

TOKENS = [
    ("INICIO", r"INICIO"),
    ("FIN", r"FIN"),
    ("SI", r"SI"),
    ("ENTONCES", r"ENTONCES"),
    ("FINSI", r"FINSI"),
    ("ESCRIBIR", r"ESCRIBIR"),
    
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
                regex = re.match(patron, self.codigo, re.IGNORECASE)  # Added re.IGNORECASE flag
                if regex:
                    coincidencia = (tipo, regex.group(0))
                    if tipo != "ESPACIO":  
                        tokens.append(coincidencia)
                    self.codigo = self.codigo[len(coincidencia[1]):]  # Fixed slicing to use the matched string length
                    break
            if not coincidencia:
                raise SyntaxError(f"Token no reconocido: {self.codigo[0]}")
        return tokens
