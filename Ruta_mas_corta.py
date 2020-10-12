def calcular_distancia(ruta: list, distancias: dict) -> float:
    caminos = [(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)]
    distancia_nodos = [distancias[camino] for camino in caminos]
    return sum(distancia_nodos)

def validar_distancia(distancias: dict) -> bool:
    for recorrido, distancia in distancias.items():
        if distancia < 0:
            return False
        elif recorrido[0] == recorrido[1] and distancia != 0:
            return False
    return True

def ruteo(distancias: dict, ruta_inicial: list) -> dict:
    if not validar_distancia(distancias):
        return "Por favor revisar los datos de entrada."

    ruta_actual = ruta_inicial.copy()
    ruta_mas_corta = ruta_inicial.copy()
    distancia_mas_corta = calcular_distancia(ruta_actual, distancias)
    mejoro = True

    while mejoro:

        ruta_ciclo = ruta_mas_corta.copy()
        ruta = ruta_mas_corta[1:-1]
        ruta_actual = ruta_mas_corta.copy()
        mejoro = False

        for i, nodo in enumerate(ruta):
            for j, destino in enumerate(ruta[i + 1:], start=i + 1):
                # print(f'Camino {(nodo, destino)} - Posición origen {i + 1} - Posición destino {j + 1}')
                ruta_actual[i + 1] = destino
                ruta_actual[j + 1] = nodo
                distancia_ruta_actual = calcular_distancia(ruta_actual, distancias)

                if distancia_ruta_actual < distancia_mas_corta:
                    distancia_mas_corta = distancia_ruta_actual
                    ruta_mas_corta = ruta_actual.copy()
                    mejoro = True

                ruta_actual = ruta_ciclo.copy()

    return {'ruta': "-".join(ruta_mas_corta), 'distancia': distancia_mas_corta}
