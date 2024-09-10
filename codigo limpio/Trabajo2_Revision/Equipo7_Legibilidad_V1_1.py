class Calculadora:
    def calculo(self, Operando1, Operando2):
        """
        Calcula el resultado de una operación basada en el valor del segundo operando.

        Si el segundo operando es cero, se realiza una división de operandos.
        De lo contrario, se realiza una multiplicación.

        :param operand1: Primer operando (número).
        param operand2: Segundo operando (número).
        :return: Resultado de la operación.
        """
        if Operando2 == 0:
            if Operando1 == 0:
                raise ValorError("No se puede dividir por cero cuando el primer operando es cero.")
            return Operando1 / Operando2
        else:
            return Operando1 * Operando2