from time import sleep
from random import expovariate
from random import gauss
from math import log
from matplotlib import pyplot as plt


def generar_exponencial(cantidad=100, beta=1):
    valores = [expovariate(beta) for _ in range(cantidad)]
    promedio = sum(valores) / len(valores)
    print(f"El promedio es: {promedio}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


def generar_gauss(cantidad=100, media=0, desvio=1):
    valores = [gauss(media, desvio) for _ in range(cantidad)]
    promedio = sum(valores) / len(valores)
    print(f"El promedio es: {promedio}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


if __name__ == "__main__":
    generar_exponencial(1000, beta=0.75)
    generar_gauss(1000, media=10, desvio=1)
