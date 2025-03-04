// Pila.h
#ifndef PILA_H
#define PILA_H

#include <list>
#include "ElementoPila.h"

class Pila {
private:
    list<ElementoPila*> lista;  // Lista que contiene los punteros a ElementoPila

public:
    // Método para agregar un elemento a la pila
    void push(ElementoPila* x) {
        lista.push_front(x);
    }

    // Método para eliminar el primer elemento de la pila
    ElementoPila* pop() {
        ElementoPila* x = *lista.begin();
        lista.erase(lista.begin());
        return x;
    }

    // Método para obtener el primer elemento de la pila
    ElementoPila* top() {
        return *lista.begin();
    }

    // Método para mostrar todos los elementos de la pila
    void muestra() {
        list<ElementoPila*>::reverse_iterator it;
        ElementoPila* x;
        cout << "Pila: " << endl;
        for (it = lista.rbegin(); it != lista.rend(); it++) {
            x = *it;
            x->muestra();
        }
        cout << endl;
    }
};

#endif
