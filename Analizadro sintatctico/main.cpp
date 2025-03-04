// principal.cpp
#include <iostream>
#include "Pila.h"
#include "Terminal.h"
#include "NoTerminal.h"
#include "Estado.h"

void ejemplo() {
    Pila pila;

    // Crear objetos de diferentes tipos
    ElementoPila* terminal = new Terminal("a");
    ElementoPila* noTerminal = new NoTerminal("S");
    ElementoPila* estado = new Estado("q0");

    // Agregar objetos a la pila
    pila.push(terminal);
    pila.push(noTerminal);
    pila.push(estado);

    // Mostrar la pila
    pila.muestra();

    cout << "*********************************" << endl;

    // Realizar un pop y mostrar la pila nuevamente
    pila.pop();
    pila.muestra();
}

int main() {
    ejemplo();  // Llamada a la función de ejemplo
    return 0;
}
