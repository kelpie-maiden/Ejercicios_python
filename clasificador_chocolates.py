def clasificador_chocolates(numero_identificacion):

    cadena = str(numero_identificacion)[::-1]
    numero_invertido = int(cadena)

    if numero_invertido == numero_identificacion:
        if numero_identificacion % 2 == 0:
            resultado = "SWEET"
        else:
            resultado = "BITTER"

    else:
        if numero_identificacion % 2 == 0:
            resultado = "CINNAMON & CLOVES"
        else:
            resultado = "LIGHT"

    return " La clasificacion del chocolate corresponde a {}".format(resultado)


