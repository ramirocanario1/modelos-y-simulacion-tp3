from time import sleep
from random import expovariate
from random import gauss
from math import log
from matplotlib import pyplot as plt


def generar_exponencial(cantidad):
    valores = [expovariate(1) for _ in range(cantidad)]
    media = sum(valores) / len(valores)
    print(f"El promedio es: {media}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


def generar_gauss(cantidad):
    valores = [gauss(0, 1) for _ in range(cantidad)]
    media = sum(valores) / len(valores)
    print(f"El promedio es: {media}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


if __name__ == "__main__":
    # Generar 1000 valores aleatorios con distribucion exponencial
    generar_exponencial(1000)
    generar_gauss(1000)
