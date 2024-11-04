"""
MINI CALCULADORA BINARIA
"""


# Se solicitan los números binarios:

binario1 = input("Introduce el primer número binario de 8 bits: ")
binario2 = input("Introduce el segundo número binario de 8 bits: ")


# Se verifica que los valores son exactamente de 8 bits:


if len(binario1) == 8 and len(binario2) == 8:
        es_valido_1 = True
        es_valido_2 = True

else:
       es_valido_1 = False
       es_valido_2 = False

# Verificar que los valores estén en binario, es decir, que contengan 0s y 1s:


for char in binario1:
        if char != '0' and char != '1':
            es_valido_1 = False #binario1 no es válido

for char in binario2:
        if char != '0' and char != '1':
            es_valido_2 = False #binario2 no es válido


if es_valido_1 and es_valido_2:
        print("Ambos números binarios son correctos.")

else:
        print("Uno o ambos números contienen caracteres que no son los correctos.")


                                        # Función para la suma en binario, con su acarreo:
def suma_binaria(binario1, binario2): 
       acarreo = 0
       resultado = ''
       
       for i in range(7, -1, -1):       
       

       




