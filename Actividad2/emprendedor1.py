#  Actividad 2- Rentabilidad
#------------------------------#
# Un emprendedor quiere crear una app que provea un servicio de entrega de comida para mascotas. Este proyecto tiene buenos pronósticos, pero 
# su éxito dependerá de cuántos usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades del proyecto. 
# Estas utilidades se pueden calcular mediante la siguiente fórmula:
 
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 - 𝐺𝑇

# Donde:
# P: Precio de Suscripción
# U: Número de Usuarios
# GT: Gastos Totales
# Para ello, se te pide desarrollar este cálculo en tres versiones.

#  1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente para calcular las utilidades de un proyecto.Para ello 
# utiliza input() para solicitar como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.


# Script
#-----------------------------------#
import math

# Mensajes
print('Nota: Ingrese las cifras sin puntos "." ni comas "," \n Si la cifra que desea ingresar es un decimal, indíquelo utilizando un punto "." ')

# Inputs
P = float(input('Ingrese el precio de suscripción: $ '))
U = int(input('Ingrese el número de usuarios: '))
GT = float(input('Ingrese el gasto total: $ '))

# Cálculo

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 - 𝐺𝑇



# Output
print(f'Las utilidades del proyecto corresponden a $ {𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠}')