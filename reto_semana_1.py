def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    """ Nota quices :
    Parámetros:
    codigo (str): codigo único alfanumérico del estudiante
    nota1 (int): Nota del primer quiz reto semestre (0 - 100) 
    nota2 (int): Nota del segundo quiz del semestre (0 - 100) 
    nota3 (int): Nota del tercer quiz del semestre (0 - 100) 
    nota4 (int): Nota del cuarto quiz del semestre (0 - 100) 
    nota5 (int): Nota del quinto quiz del semestre (0 - 100) 
    
    Retorno: 
    String: de la forma "El promedio ajustado del estudiante {codigo} es: {promedio}" dónde, el promedio se calcula eliminando
    la peor nota y se reporta con dos decimales utilizando la escala numérica de 0 a 5
    """
    notas = [nota1, nota2, nota3, nota4, nota5]

    nota_minima = min(notas)
    mejores_notas = sum(notas) - nota_minima
    nota_promedio = mejores_notas/4

    nota_equivalente = round((nota_promedio*5)/100, 2)

    return "El promedio ajustado del estudiante {} es: {}".format(codigo, nota_equivalente)

