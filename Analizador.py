import os
import re
import pandas as pd

archivo_excel = r"C:\Users\61pab\OneDrive\Documentos\Seminario de traductores II\Gramaticas_ejecicios1y2.xlsx"

# Si el archivo no existe, se crea automáticamente
if not os.path.exists(archivo_excel):
    with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
        pd.DataFrame().to_excel(writer)  # Crear un archivo vacío

print(f"Usando archivo: {archivo_excel}")

class AnalizadorLexico:
    def __init__(self, entrada):
        self.entrada = entrada
        self.tokens = []
        self.analizar()

    def analizar(self):
        patron = re.compile(r"[a-zA-Z]+|\+")
        self.tokens = patron.findall(self.entrada)

    def muestra_tokens(self):
        return self.tokens

def ejemplo2():
    entrada = "a+b+c+d+e+f"
    analizador = AnalizadorLexico(entrada)
    return analizador.muestra_tokens()

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, valor):
        self.elementos.append(valor)

    def pop(self):
        return self.elementos.pop() if self.elementos else None

    def top(self):
        return self.elementos[-1] if self.elementos else None

    def muestra(self):
        return self.elementos.copy()

def ejemplo1():
    pila = Pila()
    entrada = "hola+mundo"
    for letra in entrada:
        pila.push(letra)

    estado1 = pila.muestra()

    tope1 = pila.top()
    pop1 = pila.pop()
    pop2 = pila.pop()
    estado2 = pila.muestra()

    return estado1, tope1, pop1, pop2, estado2


tokens = ejemplo2()
estado1, tope1, pop1, pop2, estado2 = ejemplo1()

# Crear DataFrames
df_lexico = pd.DataFrame({'Tokens': tokens})

df_pila = pd.DataFrame({
    "Acción": ["Estado inicial", "Tope", "Pop 1", "Pop 2", "Estado final"],
    "Valor": [str(estado1), tope1, pop1, pop2, str(estado2)]
})

with pd.ExcelWriter(archivo_excel, engine="openpyxl", mode="w") as writer:
    df_lexico.to_excel(writer, sheet_name="Analizador_Lexico", index=False)
    df_pila.to_excel(writer, sheet_name="Pila", index=False)

print(f"Resultados guardados en {archivo_excel}")
