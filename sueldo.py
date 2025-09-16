"""
El programa calcula el sueldo mensual semanal de un empleado. Si se trabaja mas de 48 hotas, las horas 
extras se pagan al doble de la tarifa normal.
"""


# Declaraciones


# Entradas
horas_trabajadas=float(input())
tarifa=float(input())

# Proceso
if horas_trabajadas > 48:
    horas_extras = horas_trabajadas - 48
    pago_extra = horas_extras * tarifa * 2
    pago = 48 * tarifa
else:
    horas_extras = 0
    pago_extra = 0
    pago = horas_trabajadas * tarifa

total_a_pagar = pago + pago_extra

# Salidas
print(horas_extras)
print(pago_extra)
print(total_a_pagar)
