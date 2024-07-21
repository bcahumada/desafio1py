# 2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados, los usuarios normales y los usuarios premium
#    a los cuales se les cobrará una suscripción un 50% mayor. Para ello modifica la fórmula de utilidades en la cual se solicite 
#    mediante input() los parámetros de entrada precios de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.


# Script
#-----------------------------------#
import math

# Mensajes
print('Nota: No ingrese puntos "." ni comas "," para indicar los miles de la cifra \n Si la cifra que desea ingresar es un decimal, indíquelo utilizando un punto "." ')

# Inputs
P = float(input('Ingrese el precio de suscripción: $ '))
Un = int(input('Ingrese el número de usuarios normales: '))
Up = int(input('Ingrese el número de usuarios premium: '))
GT = float(input('Ingrese el gasto total: $ '))

# Cálculo

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = (𝑃 * 𝑈n) + (P * 1.5 * Up) - 𝐺𝑇


# Outputs
print(f'Las utilidades del proyecto corresponden a $ {𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠}')