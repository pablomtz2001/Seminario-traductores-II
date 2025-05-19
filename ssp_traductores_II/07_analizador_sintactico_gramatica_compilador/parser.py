import pandas as pd
import re

# Leer la tabla de análisis sintáctico desde un archivo de texto con formato CSV
parsing_table = pd.read_csv('tabla.txt', index_col=0)

# Definir los tokens válidos
tokens_validos = {
    'identificador', 'entero', 'real', 'cadena', 'tipo',
    'opSuma', 'opMul', 'opRelac', 'opOr', 'opAnd', 'opNot', 'opIgualdad',
    ';', '"', ',', '(', ')', '{', '}', '=', 'if', 'while', 'return',
    'else', '$'
}

# Verificar si un token es válido
def es_token_valido(token):
    return token in tokens_validos

# Simulación del analizador léxico que convierte una cadena en tokens
def analizador_lexico(entrada):
    patron = r'\w+|[{}(),;"=]|==|!=|<=|>=|<|>|\+|\-|\*|/|\$'
    tokens = re.findall(patron, entrada)
    tokens_filtrados = []

    for token in tokens:
        if token.isdigit():
            tokens_filtrados.append('entero')
        elif re.fullmatch(r'\d+\.\d+', token):
            tokens_filtrados.append('real')
        elif re.fullmatch(r'".*"', token):
            tokens_filtrados.append('cadena')
        elif token in {'int', 'float', 'void'}:
            tokens_filtrados.append('tipo')
        elif token in {'+', '-'}:
            tokens_filtrados.append('opSuma')
        elif token in {'*', '/'}:
            tokens_filtrados.append('opMul')
        elif token in {'<', '<=', '>', '>='}:
            tokens_filtrados.append('opRelac')
        elif token in {'||'}:
            tokens_filtrados.append('opOr')
        elif token in {'&&'}:
            tokens_filtrados.append('opAnd')
        elif token in {'!'}:
            tokens_filtrados.append('opNot')
        elif token in {'==', '!='}:
            tokens_filtrados.append('opIgualdad')
        elif token in tokens_validos:
            tokens_filtrados.append(token)
        else:
            tokens_filtrados.append('identificador')

    tokens_filtrados.append('$')
    return tokens_filtrados

# Analizador sintáctico
def analizador_sintactico(tokens):
    pila = ['$', 'programa']
    indice = 0

    while len(pila) > 0:
        cima = pila[-1]
        token_actual = tokens[indice]

        if cima == token_actual:
            pila.pop()
            indice += 1
        elif cima in parsing_table.index:
            entrada = parsing_table.loc[cima, token_actual]
            if pd.isna(entrada):
                print(f"Error de sintaxis: no se esperaba el token '{token_actual}'")
                return False
            produccion = str(entrada).split(',')
            pila.pop()
            for simbolo in reversed(produccion):
                if simbolo != 'ε':
                    pila.append(simbolo)
        else:
            print(f"Error de sintaxis: símbolo inesperado en la pila '{cima}'")
            return False

    if indice == len(tokens):
        print("Análisis sintáctico exitoso.")
        return True
    else:
        print("Error de sintaxis: tokens restantes sin analizar.")
        return False

# === Prueba ===
entrada = 'int main ( ) { return 0 ; }'
tokens = analizador_lexico(entrada)
print("Tokens:", tokens)
resultado = analizador_sintactico(tokens)
