from punto3 import generar_valores_exponenciales
from matplotlib import pyplot as plt

if __name__ == "__main__":
    for cantidad in [100, 1000, 10000]:
        valores_exponenciales = generar_valores_exponenciales(cantidad, beta=3)

        plt.hist(valores_exponenciales, bins=50, density=True)
        plt.title(
            f"Histograma de {cantidad} valores exponenciales generados con beta=3"
        )
        plt.show()
