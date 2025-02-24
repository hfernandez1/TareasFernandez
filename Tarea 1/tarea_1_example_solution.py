# Hernan I. Fernandez Castiglione
# Carné: 2022086706
# Fecha: 02/23/2025


def separa_letras(cadena):
    """
    Separa las letras de una cadena en mayúsculas y minúsculas.
    Retorna un código de éxito o error junto con las cadenas correspondientes.

    Parámetros:
        cadena (str): Cadena de entrada.

    Retorna:
        tuple: (código de estado, string de mayúsculas, string de minúsculas).
    """
    # Verifica si la entrada no es un string
    if not isinstance(cadena, str):
        return -100, None, None  # Error: No es un string válido

    # Verifica si la cadena está vacía
    if cadena == "":
        return -300, None, None  # Error: String vacío

    # Verifica si la cadena contiene caracteres que no son letras
    if not cadena.isalpha():
        return -200, None, None  # Error: Caracter fuera del abecedario

    # Extrae todas las letras mayúsculas en un solo string
    mayusculas = "".join(
        c for c in cadena if c.isupper()
    )

    # Extrae todas las letras minúsculas en un solo string
    minusculas = "".join(
        c for c in cadena if c.islower()
    )

    # Retorna el código de éxito 0
    # Retorna las cadenas de mayúsculas y minúsculas
    return 0, mayusculas, minusculas


def potencia_manual(base, potencia):
    """
    Calcula base^potencia usando sumas y ciclos
    sin multiplicaciones ni potencias.
    Retorna un código de éxito o error junto con el resultado.

    Parámetros:
        base (int): Base de la operación.
        potencia (int): Exponente.

    Retorna:
        tuple: (código de estado, resultado de la operación).
    """
    # Verifica si los parámetros de entrada son enteros
    if not isinstance(base, int) or not isinstance(potencia, int):
        return -400, None  # Error: Parámetro no es un entero

    # Caso especial: cualquier número elevado a 0 es 1
    if potencia == 0:
        return 0, 1  # Código de éxito 0

    # No se permite calcular potencias negativas en esta función
    if potencia < 0:
        return -400, None  # Error: No se aceptan exponentes negativos

    # Inicializa el resultado en 1 (ya que cualquier número elevado a 0 es 1)
    resultado = 1

    # Calcula la potencia manualmente usando sumas
    for _ in range(potencia):  # Itera tantas veces como el exponente indique
        suma = 0
        for _ in range(base):  # Realiza sumas sucesivas
            suma += resultado
        resultado = suma  # Actualiza el resultado con la nueva suma acumulada

    # Retorna el código de éxito y el resultado de la potencia
    return 0, resultado
