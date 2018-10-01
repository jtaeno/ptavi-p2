
import sys
import calcoohija

fich = open(sys.argv[1], 'r', encoding='utf-8')
lista = fich.readlines()
if __name__ == "__main__":
    for pal in lista:
        listas = pal.split(",")
        try:
            listasnum = [int(i) for i in listas[1:]]
            if listas[0] == 'suma':
                suma = 0
                for i in listasnum:
                    suma = calcoohija.Calculadorahija.plus(i, suma)
                    resultado = suma
                print("Resultado suma:", resultado)
            elif listas[0] == 'resta':
                resta = listasnum[0] * 2
                for i in listasnum:
                    resta = calcoohija.Calculadorahija.minus(resta, i)
                    resultado = resta
                print("Resultado resta:", resultado)
            elif listas[0] == 'multiplica':
                multiplica = 1
                for i in listasnum:
                    multiplica = calcoohija.Calculadorahija.mult(multiplica, i)
                    resultado = multiplica
                print("Resultado multiplicacion:", resultado)
            elif listas[0] == 'divide':
                divide = listasnum[0] * listasnum[0]
                for i in listasnum:
                    try:
                        divide = calcoohija.Calculadorahija.div(divide, i)
                        resultado = divide
                    except ZeroDivisionError:
                        resultado = "Division by zero is not allowed"
                print("Resultado division:", resultado)
            else:
                print("Las operaciones deben ser sumar restar multiplicar y dividir ")
        except ValueError:
            resultado = "Error: Non numerical parameters"
            print(resultado)
