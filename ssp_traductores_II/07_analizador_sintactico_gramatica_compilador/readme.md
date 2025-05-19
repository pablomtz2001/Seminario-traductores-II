# Analizador Sintáctico 

Este programa es un analizador sintáctico que utiliza PyQt5 para la interfaz gráfica. Permite a los usuarios introducir cadenas de texto, las cuales son analizadas para identificar tokens y estructuras sintácticas según nuestras reglas definidas. La aplicación muestra los tokens identificados y proporciona un feedback sobre la validez sintáctica de la entrada.

## Estructura del Proyecto

El proyecto consta de un único script de Python que incluye todo el código necesario para la interfaz gráfica y la lógica del analizador sintáctico. Además, se utilizan dos archivos externos (`GR2slrRulesId.txt` y `GR2slrTable.txt`) para definir las reglas y la tabla SLR utilizadas en el análisis sintáctico.

- `main.py`: Script principal que contiene la lógica del analizador sintáctico y la interfaz gráfica.
- `GR2slrRulesId.txt`: Define las reglas sintácticas.
- `GR2slrTable.txt`: Define la tabla SLR para el análisis sintáctico.


## Funcionamiento

El analizador realiza los siguientes pasos:

1. **Análisis Léxico**: Identifica tokens en la entrada del usuario basándose en caracteres específicos y transiciones de estado.
2. **Clasificación de Tokens**: Ajusta la clasificación de los tokens identificados si coinciden con palabras reservadas o son identificadores de tipos de dato.
3. **Análisis Sintáctico**: Utiliza una tabla SLR y reglas sintácticas definidas para verificar la validez sintáctica de la cadena de entrada.
4. **Resultados**: Muestra los tokens identificados en una tabla y un mensaje indicando si la cadena es válida o no desde el punto de vista sintáctico.