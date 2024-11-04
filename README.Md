## Mini-Calculadora Binaria 

**por Antonio José Monge Monge**

Descripción

**IGNORAR TEST01** es el primer programita que hicimos en clase y quería mantenerlo por si tenía que volver a él y no perder la base.

Este programa en Python es una calculadora binaria que solo permite sumar y restar números binarios de 8 bits ingresados por el usuario. Trabaja directamente con cadenas de texto que representan números binarios y realiza las operaciones bit a bit sin usar funciones de conversión ni nada por el estilo, como marcaban las restricciones.

Características:

    - Verificación de entrada: Comprueba que los números ingresados sean binarios válidos de 8 bits.
    - Suma y resta binaria: Realiza sumas y restas bit a bit, gestionando el acarreo y el préstamo.

Cómo Usarlo

    1. Ejecuta el programa en un entorno que soporte Python3.
    2. Ingresa dos números binarios de 8 bits cuando se te pida (por ejemplo, 10101010 y 11001100).
    3. Selecciona la operación que deseas realizar: sumar o restar.
    4. Observa el resultado: el programa mostrará la suma o resta en binario o indicará si el resultado es negativo.

Observaciones

Estuve dandole vueltas a la cabeza y me la rompí mucho porque no logré hacer representar cuando un resultado me salía negativo en papel, por ejemplo 00000000 - 11111111. Por lo que tuve que poner un return que imprimiese un mensaje de no es posible hacer esa resta.

Bibliografía

[Cómo hacer sumas y restas binarias](https://weblab.deusto.es/olarex/cd/UD/Puertas%20logicas_ES_final/operaciones_aritmticas_con_sistema_binario_suma_y_resta.html)

[Calculadora Binaria Online ](https://es.planetcalc.com/911/)

Y un saludo a mi amigo Álvaro que me echó un cable para la resta :D
