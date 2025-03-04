// Estado.h
#ifndef ESTADO_H
#define ESTADO_H

#include "ElementoPila.h"

class Estado : public ElementoPila {
private:
    string nombreEstado;  // Nombre del estado

public:
    Estado(string nombreEstado) : nombreEstado(nombreEstado) {}

    void muestra() override {
        cout << "Estado: " << nombreEstado << endl;
    }
};

#endif
