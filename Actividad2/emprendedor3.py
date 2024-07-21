#  3. Considera la fórmula original de utilidades:  𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 - 𝐺𝑇
 
# Crear una nueva función en la que se pida (por medio de input()) los siguientes datos:
# ● precio de suscripción P
# ● número de usuarios normales U
# ● gastos GT
# ● utilidades del año anterior Uanterior
 
# El programa debe calcular las utilidades actuales Uactuales y mostrar la razón entre las utilidades actuales y las del año anterior
# 𝑅𝑎𝑧ó𝑛 = 𝑈𝑎𝑐𝑡𝑢𝑎𝑙𝑒𝑠 𝑈𝑎𝑛𝑡𝑒𝑟𝑖𝑜𝑟

# El resultado debe estar redondeado a dos decimales.
import math

# Script
#-----------------------------------#

# Mensajes
print('Nota: Ingrese las cifras sin puntos "." ni comas "," ')

# Inputs
P = float(input('Ingrese el precio de suscripción: $ '))
U = int(input('Ingrese el número de usuarios normales: '))
GT = float(input('Ingrese el gasto total: $ '))
Uanterior = float(input('Ingrese las utilidades del año anterior \n *Las utilidades deben ser distintas de cero "0": $ '))

# Cálculo

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = round((𝑃 * 𝑈 - 𝐺𝑇),2)

Uactuales = 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠
𝑅𝑎𝑧o𝑛 = round((𝑈𝑎ctuales/Uanterior), 2)



# Output
print(f'Las utilidades actuales del proyecto corresponden a $ {Uactuales}')
print(f'La razón entre las utilidades actuales y las del proyecto anterior es {Razon}')