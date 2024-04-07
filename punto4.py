from punto3 import generar_valores_exponenciales
from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
        Código copiado de punto3_comparacion.py
        Solo se calculan los valores solicitados en el enunciado y se agregan al gráfico
    """
    for cantidad in [100, 1000, 10000]:
        valores_exponenciales = generar_valores_exponenciales(cantidad, beta=3)

        media_muestral = sum(valores_exponenciales) / len(valores_exponenciales)
        desvio_estandar = (sum((valor - media_muestral) ** 2 for valor in valores_exponenciales) / len(valores_exponenciales)) ** 0.5
        varianza = desvio_estandar ** 2

        plt.hist(valores_exponenciales, bins=50, density=True)
        plt.title(
            f"Histograma de {cantidad} valores exponenciales generados con beta=3"
        )
        plt.text(0.5, 0.95, f"Media muestral: {media_muestral:.2f}", ha='center', va='top', transform=plt.gca().transAxes)
        plt.text(0.5, 0.9, f"Desvio estandar: {desvio_estandar:.2f}", ha='center', va='top', transform=plt.gca().transAxes)
        plt.text(0.5, 0.85, f"Varianza: {varianza:.2f}", ha='center', va='top', transform=plt.gca().transAxes)
        plt.show()
