// ElementoPila.h
#ifndef ELEMENTO_PILA_H
#define ELEMENTO_PILA_H

#include <iostream>
using namespace std;

class ElementoPila {
public:
    virtual void muestra() = 0;  // Método virtual puro para mostrar detalles
    virtual ~ElementoPila() {}    // Destructor virtual para manejar liberación de memoria
};

#endif
