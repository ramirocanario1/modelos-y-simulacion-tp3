from random import randint
from time import sleep

if __name__ == "__main__":

    numeros_aleatorios = []

    for i in range(100):
        numeros_aleatorios.append(randint(1, 100))

    promedio = sum(numeros_aleatorios) / len(numeros_aleatorios)
    desvio_estandar = (
        sum([(x - promedio) ** 2 for x in numeros_aleatorios]) / len(numeros_aleatorios)
    ) ** 0.5
    varianza = desvio_estandar**2

    print(f"Promedio: {promedio}")
    print(f"Desvio estandar: {desvio_estandar}")
    print(f"Varianza: {varianza}")

    # Generar graficos
    import matplotlib.pyplot as plt

    plt.hist(numeros_aleatorios, bins=100)
    plt.show()
    input("Presione enter para salir")
