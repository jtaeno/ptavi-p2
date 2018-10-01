#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class Calculadorahija(calcoo.Calculadora):
    def mult(op1, op2):
        return op1 * op2

    def div(op1, op2):
        return op1 / op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = Calculadorahija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = Calculadorahija.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = Calculadorahija.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        if sys.argv[3] != '0':
            result = Calculadorahija.div(operando1, operando2)
        else:
            sys.exit("Division by zero is not allowed")
    else:
        sys.exit('Operación sólo puede ser sumar restar multiplicar o dividir.')

    print(result)
