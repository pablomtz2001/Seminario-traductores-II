// NoTerminal.h
#ifndef NOPRUEBA_H
#define NOPRUEBA_H

#include "ElementoPila.h"

class NoTerminal : public ElementoPila {
private:
    string simbolo;  // El símbolo que representa este no terminal

public:
    NoTerminal(string simbolo) : simbolo(simbolo) {}

    void muestra() override {
        cout << "No Terminal: " << simbolo << endl;
    }
};

#endif
