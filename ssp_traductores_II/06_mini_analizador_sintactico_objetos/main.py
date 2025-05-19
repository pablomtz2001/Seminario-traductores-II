class ElementoPila:
    pass

class Terminal(ElementoPila):
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"Terminal('{self.symbol}')"

class NoTerminal(ElementoPila):
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"NoTerminal('{self.symbol}')"

class Estado(ElementoPila):
    def __init__(self, state):
        self.state = state

    def __repr__(self):
        return f"Estado({self.state})"

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        if isinstance(item, ElementoPila):
            self.items.append(item)
        else:
            raise TypeError("Only objects of type ElementoPila can be pushed onto the stack.")

    def pop(self):
        if self.items:
            return self.items.pop()

    def top(self):
        if self.items:
            return self.items[-1]

    def __repr__(self):
        return str(self.items)

class SyntacticAnalyzerOO:
    def __init__(self, action_table, goto_table, grammar_rules):
        self.action = action_table
        self.goto = goto_table
        self.grammar = grammar_rules
        self.stack = Pila()
        self.stack.push(Estado(0))

    def parse(self, tokens):
        cursor = 0

        while True:
            #print(self.stack, tokens[cursor:])
            top_state = self.stack.top()
            symbol = tokens[cursor] if cursor < len(tokens) else Terminal('$')
            action_entry = (top_state.state, symbol.symbol)

            if action_entry in self.action:
                action, value = self.action[action_entry]

                if action == 's':  # Shift action
                    self.stack.push(symbol)  # Shift symbol
                    self.stack.push(Estado(value))  # Shift state
                    cursor += 1

                elif action == 'r':  # Reduce action
                    for _ in range(self.grammar[value][1] * 2):
                        self.stack.pop()  # Pop state and symbol
                    non_terminal = NoTerminal(self.grammar[value][0])
                    self.stack.push(non_terminal)
                    goto_state = self.stack.items[-2].state
                    goto_entry = (goto_state, non_terminal.symbol)
                    self.stack.push(Estado(self.goto[goto_entry]))

                elif action == 'acc':  # Accept action
                    print("The input string is accepted by the grammar.")
                    return True

            else:
                print("The input string is not accepted by the grammar.")
                return False

        return False

# Function to tokenize the input string
def tokenize(input_string):
    tokens = []
    current_token = ''
    for char in input_string:
        if char.isalpha() or char.isdigit():
            current_token += char
        else:
            if current_token:
                tokens.append(Terminal('id'))
                current_token = ''
            if char in ['+', '$']:
                tokens.append(Terminal(char))
    if current_token:
        tokens.append(Terminal('id'))
    tokens.append(Terminal('$'))  # End of input
    return tokens

action_table_grammar_1 = {
    (0, 'id'): ('s', 2),
    (1, '$'): ('acc', ''),
    (2, '+'): ('s', 3),
    (3, 'id'): ('s', 4),
    (4, '$'): ('r', 'E -> id + id')
}

goto_table_grammar_1 = {
    (0, 'E'): 1
}

grammar_rules_grammar_1 = {
    'E -> id + id': ('E', 3) 
}

action_table_grammar_2 = {
    (0, 'id'): ('s', 2),
    (1, '$'): ('acc', ''),
    (2, '+'): ('s', 3),
    (2, '$'): ('r', 'E -> id'),
    (3, 'id'): ('s', 2),
    (4, '$'): ('r', 'E -> id + E')
}

goto_table_grammar_2 = {
    (0, 'E'): 1,
    (3, 'E'): 4
}

grammar_rules_grammar_2 = {
    'E -> id': ('E', 1),       # E -> id reduces 1 item from stack
    'E -> id + E': ('E', 3)  
}

analyzer_grammar_1 = SyntacticAnalyzerOO(action_table_grammar_1, goto_table_grammar_1, grammar_rules_grammar_1)
analyzer_grammar_2 = SyntacticAnalyzerOO(action_table_grammar_2, goto_table_grammar_2, grammar_rules_grammar_2)

tokens_1 = tokenize('hola+mundo+cruel')
tokens_2 = tokenize('a+b+c+d+e++')

analyzer_grammar_1.parse(tokens_1)
analyzer_grammar_2.parse(tokens_2)
