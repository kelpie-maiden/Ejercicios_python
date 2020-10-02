def parqueadero_buses(cantidad_buses, numero_bus):
    """
    cantidad_buses = int - tamaño del parqueadero
    numero_bus = int - el numero unico del bus a ubicar en alguno de los tres lotes del parqueo
    """
    p = cantidad_buses % 3 == 0
    q = cantidad_buses >= numero_bus > 0
    r = isinstance(numero_bus, int)
    s = isinstance(cantidad_buses, int)

    if p and q and r and s:
        if numero_bus <= cantidad_buses / 3:
            resultado = 1

        elif numero_bus <= cantidad_buses * 2 / 3:
            resultado = 2

        else:
            resultado = 3

    else:
        resultado = "-No disponible-"

    return "La zona de parqueadero a usar es {}".format(resultado)

