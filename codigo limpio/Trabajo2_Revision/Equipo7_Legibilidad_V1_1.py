class Calculadora:
    def calculo(self, operando1, operando2):

        """
         Realiza una multiplicación si operando2 es diferente de 1.
        Realiza una división si operando2 es igual a 1.
        Lanza una excepción si operando2 es cero.
        """

        if operando2 == 0:
            if operando1 == 0:
                raise ZeroDivisionError("El divisor no puede ser cero")
            return operando1 / operando2
        else:
            return operando1 * operando2


if __name__ == "__main__":
    try:
        operando1 = float(input("Introduce el primer operando:  "))
        operando2 = float(input("Introduce el segundo operando:  "))


        calculadora = Calculadora()

        resultado = calculadora.calculo(operando1, operando2)

        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
    except ZeroDivisionError as error:
        print(error)