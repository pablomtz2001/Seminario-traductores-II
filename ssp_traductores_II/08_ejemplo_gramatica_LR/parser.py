import pandas as pd

parsing_table = pd.read_csv('compilador.csv', index_col=0)

parsing_table.fillna("error", inplace=True)

reducciones= {
    1: ('programa', 1),
    2: ('Definiciones', 1),
    3: ('Definiciones ', 2),
    4: ('Definicion', 1),
    5: ('Definicion', 1),
    6: ('DefVar', 4),
    7: ('ListaVar', 1),
    8: ('ListaVar', 3),
    9: ('DefFunc', 6),
    10: ('Parametros', 1),
    11: ('Parametros', 3),
    12: ('ListaParam', 0),
    13: ('ListaParam', 4),
    14: ('BloqFunc', 3),
    15: ('DefLocales', 1),
    16: ('DefLocales', 2),
    17: ('DefLocal', 1),
    18: ('DefLocal', 1),
    19: ('Sentencias', 0),
    20: ('Sentencias', 2),
    21: ('Sentencia', 4),
    22: ('Sentencia', 6),
    23: ('Sentencia', 5),
    24: ('Sentencia', 3),
    25: ('Sentencia', 2),
    26: ('Otro', 1),
    27: ('Otro', 2),
    28: ('Bloque', 3),
    29: ('ValorRegresa', 1),
    30: ('ValorRegresa', 1),
    31: ('Argumentos', 1),
    32: ('Argumentos', 2),
    33: ('ListaArgumentos', 1),
    34: ('ListaArgumentos', 3),
    35: ('Termino', 1),
    36: ('Termino', 1),
    37: ('Termino', 1),
    38: ('Termino', 1),
    39: ('Termino', 1),
    40: ('LlamadaFunc', 4),
    41: ('SentenciaBloque', 1),
    42: ('SentenciaBloque', 1),
    43: ('Expresion', 3),
    44: ('Expresion', 2),
    45: ('Expresion', 2),
    46: ('Expresion', 3),
    47: ('Expresion', 3),
    48: ('Expresion', 3),
    49: ('Expresion', 3),
    50: ('Expresion', 3),
    51: ('Expresion', 3),
    52: ('Expresion', 1)
}

class Pila:
    def __init__(self):
        self.pila = []
    
    def push(self, elemento):
        self.pila.append(elemento)
    
    def pop(self):
        return self.pila.pop()
    
    def top(self):
        return self.pila[-1]
    
def analizar(tokens):
    pila = Pila()
    pila.push(0)
    i = 0
    longitud = len(tokens)
    acepted = False

    while i < longitud:
        print(pila.pila)
        token = tokens[i]
        estado = pila.top()
        accion = parsing_table.loc[estado, token.simbolo]
        if accion == 'r0':
            acepted = True
            break
        elif accion[0] == 'd':
            pila.push(token.simbolo)
            pila.push(int(accion[1:]))
            i += 1
        elif accion[0] == 'r':
            regla = int(accion[1:])
            regla = reducciones[regla]
            no_terminal = regla[0]
            for _ in range(regla[1]*2):
                pila.pop()
            print(pila.pila)
            estado = pila.top()
            pila.push(no_terminal)
            print(f"No terminal: {no_terminal}")
            print(f"Estado: {estado}")
            pila.push(parsing_table.loc[estado, no_terminal])
        else:
            break
    return acepted


