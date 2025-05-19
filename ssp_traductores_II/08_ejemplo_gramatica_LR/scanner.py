def es_letra(c):
    return c.isalpha()

def es_digito(c):
    return c.isdigit()

def es_espacio(c):
    return c in ' \t\n\r'

def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def es_numero_real(cadena):
    if '.' in cadena:
        try:
            float(cadena)
            return True
        except ValueError:
            return False
    else:
        return False
        

tabla_simbolos = {
    "int": ("tipo", 4), "float": ("tipo", 4), "void": ("tipo", 4), 
    "+": ("opSuma", 5), "-": ("opSuma", 5), 
    "*": ("opMul", 6), "/": ("opMul", 6),
    "<": ("opRelac", 7), "<=": ("opRelac", 7), ">": ("opRelac", 7), ">=": ("opRelac", 7), 
    "||": ("opOr", 8), 
    "&&": ("opAnd", 9),
    "!": ("opNot", 10),
    "==": ("opIgualdad", 11), "!=": ("opIgualdad", 11),
    ";": (";", 12), 
    ",": (",", 13),
    "(": ("(", 14), 
    ")": (")", 15),
    "{": ("{", 16),
    "}": ("}", 17),
    "=": ("=", 18),
    "if": ("if", 19), 
    "while": ("while", 20),
    "return": ("return", 21),
    "else": ("else", 22),
    "$": ("$", 23)
}

palabras_reservadas = ["int", "float", "void", "if", "while", "return", "else"]

simbolos = ["+", "-", "*", "/", "<", "<=", ">", ">=", "||", "&&", "!", "==", "!=", ";", ",", "(", ")", "{", "}", "=", "$", "&", "|"]

class Token:
    def __init__(self, lexema, simbolo, numero):
        self.lexema = lexema
        self.simbolo = simbolo
        self.numero = numero 
    
    def __str__(self):
        return f"( Token: {self.lexema}, {self.simbolo}, {self.numero} )"
    
    def __repr__(self):
        return str(self)

def obtener_tokens(codigo):
    
    i = 0
    longitud = len(codigo)
    tokens = []

    while i < longitud:
        if es_espacio(codigo[i]):
            i += 1
            continue
        
        current_token = ""
        
        if es_letra(codigo[i]):
            while i < longitud and (es_letra(codigo[i]) or es_digito(codigo[i])):
                current_token += codigo[i]
                i += 1

            if current_token in palabras_reservadas:
                tokens.append(Token(current_token, tabla_simbolos[current_token][0], tabla_simbolos[current_token][1]))
            else:
                tokens.append(Token(current_token, "identificador", 0))
        elif es_digito(codigo[i]):
            cuenta_puntos = 0
            while i < longitud and (es_digito(codigo[i]) or (codigo[i] == '.' and cuenta_puntos < 1)):
                if codigo[i] == '.':
                    cuenta_puntos += 1

                current_token += codigo[i]
                if cuenta_puntos > 1:
                    break
                i += 1
            
            if cuenta_puntos == 0:
                tokens.append(Token(current_token, "entero", 0))
            elif cuenta_puntos == 1:
                tokens.append(Token(current_token, "real", 0))
            else:
                tokens.append(Token(current_token, "error", -1))
        else:
            current_token = codigo[i]
            if current_token not in simbolos:
                tokens.append(Token(current_token, "error", -1))
                i += 1
            else:
                if (i + 1) < longitud and (current_token + codigo[i + 1]) in simbolos:
                    i += 1
                    current_token += codigo[i]
                    tokens.append(Token(current_token, current_token, tabla_simbolos[current_token][1]))
                    i += 1
                else:
                    tokens.append(Token(current_token, current_token, tabla_simbolos[current_token][1]))
                    i += 1
            
    return tokens

