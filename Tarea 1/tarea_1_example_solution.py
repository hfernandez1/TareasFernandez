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
    if not isinstance(cadena, str):
        return -100, None, None  # Código de error: No es un string válido

    if cadena == "":
        return -300, None, None  # Código de error: String vacío

    if not cadena.isalpha():
        return -200, None, None  # Código de error: Caracter no del abecedario

    mayusculas = "".join(
        c for c in cadena if c.isupper()
    )
    minusculas = "".join(
        c for c in cadena if c.islower()
    )

    return 0, mayusculas, minusculas  # Código de éxito 0


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
    if not isinstance(base, int) or not isinstance(potencia, int):
        return -400, None  # Código de error: Parámetro no es un entero

    if potencia == 0:
        return 0, 1  # Código de éxito: Cualquier número elevado a 0 es 1

    if potencia < 0:
        return -400, None  # Código de error: No se pueden exponentes negativos

    resultado = 1
    for _ in range(potencia):
        suma = 0
        for _ in range(base):
            suma += resultado
        resultado = suma

    return 0, resultado  # Código de éxito 0
