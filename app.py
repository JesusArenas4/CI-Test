def calcular_prioridad(dias_abierto ):
    if dias_abierto < 0:
        return "error: dias negativos"
    if dias_abierto > 5:
        return "prioridad alta"
    else: 
        return "prioridad normal"