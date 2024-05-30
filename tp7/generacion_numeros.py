

from math import sqrt, log, sin, cos, pi, exp
import random

def generar_numero_exponencial(promedio):
    """
    Genera un número aleatorio con distribución exponencial
    :param promedio: Promedio de la distribución exponencial
    :return: Número aleatorio
    """
    u = random.random()
    return -promedio * log(u)


def generar_numero_normal(media, desvio):
    """
    Genera un número aleatorio con distribución normal
    :param media: Media de la distribución normal
    :param desvio: Desvío estándar de la distribución normal
    :return: Número aleatorio
    """
    u1 = random.random()
    u2 = random.random()
    return media + desvio * sqrt(-2 * log(u1)) * cos(2 * pi * u2)