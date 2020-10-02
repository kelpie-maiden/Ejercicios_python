def prestamo(informacion: dict) -> dict:
    id_prestamo = informacion.get("id_prestamo")
    casado = informacion.get("casado")
    dependientes = informacion.get("dependientes")
    educacion = informacion.get("educacion")
    independiente = informacion.get("independiente")
    ingreso_deudor = informacion.get("ingreso_deudor")
    ingreso_codeudor = informacion.get("ingreso_codeudor")
    cantidad_prestamo = informacion.get("cantidad_prestamo")
    plazo_prestamo = informacion.get("plazo_prestamo")
    historia_credito = informacion.get("historia_credito")
    tipo_propiedad = informacion.get("tipo_propiedad")

    if independiente == "Si":
        independiente = True
    else:
        independiente = False

    if casado == "Si":
        casado = True
    else:
        casado = False

    if educacion == "Graduado":
        educacion = True
    else:
        educacion = False

    if tipo_propiedad == "Urbano":
        tipo_propiedad = 1
    elif tipo_propiedad == "Rural":
        tipo_propiedad = 2
    else:
        tipo_propiedad = 3

    if dependientes == "3+":
        dependientes = 3

    if historia_credito == 1:
        historia_credito = True
    else:
        historia_credito = False

    if historia_credito:
        if ingreso_codeudor > 0 and ingreso_deudor/9 > cantidad_prestamo:
            resultado = True
        else:
            if dependientes > 2 and independiente:
                if ingreso_codeudor/12 > cantidad_prestamo:
                    resultado = True
                else:
                    resultado = False
            else:
                if cantidad_prestamo < 200:
                    resultado = True
                else:
                    resultado = False
    else:
        if independiente:
            if not (casado and dependientes > 1):
                if ingreso_deudor / 10 > cantidad_prestamo or ingreso_codeudor / 10 > cantidad_prestamo:
                    if cantidad_prestamo < 180:
                        resultado = True
                    else:
                        resultado = False
                else:
                    resultado = False
            else:
                resultado = False
        else:
            if tipo_propiedad != 3 and dependientes < 2:
                if educacion:
                    if ingreso_deudor / 11 > cantidad_prestamo and ingreso_codeudor / 11 > cantidad_prestamo:
                        resultado = True
                    else:
                        resultado = False
                else:
                    resultado = False
            else:
                resultado = False

    return dict(id_prestamo=id_prestamo, aprobado=resultado)


