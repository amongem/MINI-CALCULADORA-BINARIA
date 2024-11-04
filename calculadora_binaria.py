"""
MINI-CALCULADORA BINARIA.
"""

def validar_binario(binario):
    """Verifica si el número binario tiene 8 bits y solo contiene 0s y 1s."""
    if len(binario) != 8:
        return False
    for char in binario:
        if char != '0' and char != '1':
            return False
    return True

def suma_binaria(bin1, bin2):
    """Realiza la suma binaria de dos números binarios de 8 bits."""
    acarreo = '0'
    resultado = ''

    # Recorremos los bits desde el último al primero
    for i in range(7, -1, -1):
        bit1 = bin1[i]
        bit2 = bin2[i]

        # Suma bit a bit con acarreo
        if bit1 == '1':
            if bit2 == '1':
                if acarreo == '1':
                    resultado = '1' + resultado
                    acarreo = '1'
                else:
                    resultado = '0' + resultado
                    acarreo = '1'
            else:  # bit2 es '0'
                if acarreo == '1':
                    resultado = '0' + resultado
                    acarreo = '1'
                else:
                    resultado = '1' + resultado
                    acarreo = '0'
        else:  # bit1 es '0'
            if bit2 == '1':
                if acarreo == '1':
                    resultado = '0' + resultado
                    acarreo = '1'
                else:
                    resultado = '1' + resultado
                    acarreo = '0'
            else:  # bit1 y bit2 son '0'
                if acarreo == '1':
                    resultado = '1' + resultado
                    acarreo = '0'
                else:
                    resultado = '0' + resultado

    return resultado

def resta_binaria(bin1, bin2):
    """Realiza la resta binaria de dos números binarios de 8 bits."""
    acarreo = '0'
    resultado = ''

    # Recorremos los bits desde el último al primero
    for i in range(7, -1, -1):
        bit1 = bin1[i]
        bit2 = bin2[i]

        if acarreo == '1':  # Tenemos un acarreo
            if bit1 == '0':
                if bit2 == '1':
                    resultado = '0' + resultado
                    acarreo = '1'
                else:
                    resultado = '1' + resultado
                    acarreo = '0'
            else:  
                if bit2 == '1':
                    resultado = '0' + resultado
                    acarreo = '0'
                else:
                    resultado = '1' + resultado
                    acarreo = '0'
        else:  # Sin acarreo
            if bit1 < bit2:  # Necesitamos prestado
                resultado = '1' + resultado
                acarreo = '1'
            else:
                if bit1 == bit2:
                    resultado = '0' + resultado
                else:
                    resultado = '1' + resultado
                acarreo = '0'

    return resultado

def main():
    """Función principal que ejecuta la calculadora binaria."""
    binario1 = input("Introduce el primer número binario de 8 bits: ")
    binario2 = input("Introduce el segundo número binario de 8 bits: ")

    # Validación de los números binarios
    if validar_binario(binario1) and validar_binario(binario2):
        print("Ambos números binarios son correctos.")
        operacion = input("¿Deseas sumar o restar los números binarios? (Escribe 'sumar' o 'restar'): ").lower()

        if operacion == 'sumar':
            resultado = suma_binaria(binario1, binario2)
            print(f"La suma binaria de {binario1} y {binario2} es: {resultado.zfill(8)}")
        elif operacion == 'restar':
            resultado = resta_binaria(binario1, binario2)
            print(f"La resta binaria de {binario1} y {binario2} es: {resultado.zfill(8)}")
        else:
            print("Operación no válida. Por favor, elige 'sumar' o 'restar'.")
    else:
        print("Uno o ambos números contienen caracteres que no son los correctos o no tienen 8 bits.")

if __name__ == "__main__":
    main()
