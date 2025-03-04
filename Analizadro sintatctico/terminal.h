// Terminal.h
#ifndef TERMINAL_H
#define TERMINAL_H

#include "ElementoPila.h"

class Terminal : public ElementoPila {
private:
    string simbolo;  // El símbolo que representa este terminal

public:
    Terminal(string simbolo) : simbolo(simbolo) {}

    void muestra() override {
        cout << "Terminal: " << simbolo << endl;
    }
};

#endif
