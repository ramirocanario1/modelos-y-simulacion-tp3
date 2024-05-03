from random import random, expovariate
from math import log
from matplotlib import pyplot as plt


def generar_valores_uniformes(cantidad, a, b):
    return [random() * (b - a) + a for _ in range(cantidad)]


def generar_valores_exponenciales(cantidad, beta):
    return [expovariate(beta) for _ in range(cantidad)]


def transformar_a_exponencial(valores, beta):
    return [-beta * log(1 - valor) for valor in valores]


if __name__ == "__main__":
    valores = generar_valores_uniformes(1000, 0, 1)
    valores_transformados = transformar_a_exponencial(valores, 12)

    plt.hist(valores_transformados, bins=50, density=True)
    plt.title("Histograma de valores transformados a exponencial con beta=12")
    plt.show()

    valores_exponenciales = generar_valores_exponenciales(100, beta=3)
    valores_uniformes = generar_valores_uniformes(1000, 0, 100)

    plt.hist(valores_exponenciales, bins=50, density=True)
    plt.title("Histograma de valores exponenciales generados con beta=3")
    plt.show()

    plt.hist(valores_uniformes, bins=50, density=True)
    plt.title("Histograma de valores uniformes generados entre 0 y 100")
    plt.show()
