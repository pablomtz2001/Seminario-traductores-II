class SyntacticAnalyzer:
    def __init__(self, action, goto, grammar):
        #Definimos la matriz de transición de la gramática 
        self.action = action
        self.goto = goto
        self.grammar = grammar


    def parse(self, tokens):
        stack = [0] #Definimos la pila con un simbolo inicial
        cursor = 0 #Cursor para iterar la cadena

        while True:
            print(stack)
            state = stack[-1]  # Estado Actual
            symbol = tokens[cursor] if cursor < len(tokens) else '$'  # Simbolo Actual (si la cadena no ha sido analizada copletamente se agrega un simbolo terminal)

            if (state, symbol) in self.action:
                action, value = self.action[(state, symbol)]

                if action == 's':  # Cambio de estado
                    stack.append(symbol)  # Apilamos el simbolo
                    stack.append(value)   # Apilamos el estado actual
                    cursor += 1  # Nos movemos al siguiente simbolo

                elif action == 'r':  # Acción de reducción
                    # Aplicamos la regla de la gramática
                    rule_length = self.grammar[value][1]
                    # Desapilamos el doble de reducciones ya que cada símbolo también apiló un estado
                    for _ in range(rule_length * 2):
                        stack.pop()

                    non_terminal = self.grammar[value][0]
                    # Apilamos un simbolo no terminal y nos movemos a otro estado
                    stack.append(non_terminal)
                    stack.append(self.goto[(stack[-2], non_terminal)])

                elif action == 'acc':  # Aceptamos la cadena según la gramática
                    print("The input string is accepted by the grammar.")
                    return True

            else: #Rechazamos la cadena
                print("The input string is not accepted by the grammar.")
                return False

# Función para obtener los tokens
def tokenize(input_string):
    tokens = []
    current_token = ''
    for char in input_string:
        if char.isalpha() or char.isdigit():
            current_token += char
        else:
            if current_token:
                tokens.append('id')
                current_token = ''
            if char == '+':
                tokens.append(char)
    if current_token:
        tokens.append('id')
    tokens.append('$')  # Final de la cadena
    return tokens

# Definimos la gramática del ejemplo 1
action_table1 = {
    (0, 'id'): ('s', 2),
    (1, '$'): ('acc', ''),
    (2, '+'): ('s', 3),
    (3, 'id'): ('s', 4),
    (4, '$'): ('r', 'E -> id + id')
}
goto_table1 = {
            (0, 'E'): 1
}
grammar_rules1 = {
    'E -> id + id': ('E', 3)  # E -> id + id reduce 3 elementos de la pila
}

# Definimos la gramática del ejemplo 2
action_table2 = {
    (0, 'id'): ('s', 2),
    (1, '$'): ('acc', ''),
    (2, '+'): ('s', 3),
    (2, '$'): ('r', 'E -> id'),
    (3, 'id'): ('s', 2),
    (4, '$'): ('r', 'E -> id + E')
}
goto_table2 = {
    (0, 'E'): 1,
    (3, 'E'): 4
}
grammar_rules2 = {
    'E -> id': ('E', 1),       # E -> id reduce 1 elemento de la pila
    'E -> id + E': ('E', 3)    # E -> id + E reduce 3 elementos de la pila
}

# Analizamos la primera gramática
analyzer = SyntacticAnalyzer(action_table1, goto_table1, grammar_rules1)
tokens = tokenize('hola+mundo+cruel')
result = analyzer.parse(tokens)

# Analizamos la segunda gramática
analyzer = SyntacticAnalyzer(action_table2, goto_table2, grammar_rules2)
tokens = tokenize('a+b+c+d+e+')
result = analyzer.parse(tokens)