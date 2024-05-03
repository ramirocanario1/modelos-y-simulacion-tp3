from time import sleep
from random import expovariate, gauss, random
from matplotlib import pyplot as plt
from math import exp


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


def generar_poisson(cantidad=100, l=1):
    valores = []
    for _ in range(cantidad):
        i = 0
        p = 1
        while p >= exp(-l):
            p *= random()
            i += 1
        valores.append(i)
    promedio = sum(valores) / len(valores)
    print(f"El promedio es: {promedio}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


def generar_uniforme(cantidad=100, a=0, b=1):
    valores = [random() * (b - a) + a for _ in range(cantidad)]
    promedio = sum(valores) / len(valores)
    print(f"El promedio es: {promedio}")
    plt.hist(valores, bins=50, density=True)
    plt.show()


if __name__ == "__main__":
    generar_exponencial(1000, beta=0.75)
    generar_gauss(1000, media=10, desvio=1)
    generar_poisson(1000, l=1)
    generar_uniforme(1000, a=0, b=1)
