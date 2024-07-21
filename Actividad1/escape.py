#  Actividad 1- Velocidad de escape
#-----------------------------------#

#La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad.
#La velocidad de escape se calcula mediante la siguiente fórmula:
# 𝑉𝑒 = raíz de (2𝑔r)

# Ve: corresponde a la Velocidad de Escape en [m/s].
# g: corresponde a la constante gravitacional en [m/s2].
# r: Corresponde al radio del planeta en [m].

# Requerimientos
#-----------------------------------#

# 1.  Calcular la velocidad de escape ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
#     deben ingresarse de manera interactiva utilizando la función input().

# 2. El programa debe especificar claramente el formato en el que se deben entregar los datos de entrada con instrucciones apropiadas.


# Script
#-----------------------------------#
import math

# Inputs
r = float(input('Ingrese el radio del planeta "r" en kilómetros: '))
g = float(input('Ingrese la constante gravitacional "g" en metros por segundo cuadrado: '))

# Cálculo
r= r*1000
Ve = round((2 * g * r) ** (1 / 2), 1) 


# Output
print(f'La velocidad de escape es de {Ve} [m/s]')

