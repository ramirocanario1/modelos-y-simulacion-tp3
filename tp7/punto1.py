from generacion_numeros import generar_numero_exponencial, generar_numero_normal
import random
import matplotlib.pyplot as plt


def get_tiempo_atencion_surtidor(surtidor):
    minutos = 0
    if surtidor == 1:
        minutos = generar_numero_normal(18, 4)
    elif surtidor == 2:
        minutos = generar_numero_exponencial(15)
    elif surtidor == 3:
        minutos = generar_numero_exponencial(16)
    elif surtidor == 4:
        minutos = generar_numero_normal(14, 3)
    return int(minutos)


def get_estado_surtidor(numero_surtidor):
    global surtidores_ocupados
    return surtidores_ocupados[numero_surtidor - 1]


def ocupar_surtidor(numero_surtidor):
    global surtidores, tiempo
    surtidores[numero_surtidor]["ocupado"] = True
    surtidores[numero_surtidor]["se_libera_en"] = tiempo + get_tiempo_atencion_surtidor(numero_surtidor)


def liberar_surtidor(numero_surtidor):
    global surtidores_ocupados
    surtidores_ocupados[numero_surtidor - 1] = False


def elegir_surtidor():
    global surtidores
    surtidores_libres = [surtidor for surtidor in surtidores if not surtidores[surtidor]["ocupado"]]
    if len(surtidores_libres) == 0:
        raise Exception("No hay surtidores libres")
    return surtidores_libres[random.randint(0, len(surtidores_libres) - 1)]


def get_tiempo_llegada_proximo_camion():
    global tiempo

    exponencial = int(generar_numero_exponencial(15))
    if exponencial == 0:
        exponencial = 1

    return tiempo + exponencial


def verificar_ocupacion_surtidores():
    global surtidores, tiempo
    hay_alguno_libre = False
    for surtidor in surtidores:
        if surtidores[surtidor]["ocupado"]:
            if surtidores[surtidor]["se_libera_en"] == tiempo:
                print(f"Surtidor {surtidor} liberado")
                surtidores[surtidor]["ocupado"] = False
                surtidores[surtidor]["se_libera_en"] = 0
        else:
            hay_alguno_libre = True
    return hay_alguno_libre

def mostrar_estado_surtidores():
    global surtidores
    print(f"[1] {'Ocupado' if surtidores[1]['ocupado'] else 'Libre'}, [2] {'Ocupado' if surtidores[2]['ocupado'] else 'Libre'}, [3] {'Ocupado' if surtidores[3]['ocupado'] else 'Libre'}, [4] {'Ocupado' if surtidores[4]['ocupado'] else 'Libre'}")

def obtener_tiempo_espera_promedio():
    global camiones_atendidos
    tiempo_espera_total = 0
    for camion in camiones_atendidos:
        tiempo_espera_total += camion["tiempo_atencion"] - camion["tiempo_llegada"]
    return tiempo_espera_total / len(camiones_atendidos)

def generar_grafico_tiempo_espera():
  global camiones_atendidos
  tiempos_llegada = [camion["tiempo_llegada"] for camion in camiones_atendidos]
  tiempos_atencion = [camion["tiempo_atencion"] for camion in camiones_atendidos]
  tiempos_espera = [tiempos_atencion[i] - tiempos_llegada[i] for i in range(len(tiempos_llegada))]

  plt.bar(range(len(tiempos_espera)), tiempos_espera)
  plt.ylabel('Tiempo de espera')
  plt.show()

HORAS_DIARIAS = 12
DIAS_SIMULADOS = 100
MINUTOS_SIMULADOS = HORAS_DIARIAS * 60 * DIAS_SIMULADOS

surtidores = {
    1: {"ocupado": False, "se_libera_en": 0},
    2: {"ocupado": False, "se_libera_en": 0},
    3: {"ocupado": False, "se_libera_en": 0},
    4: {"ocupado": False, "se_libera_en": 0},
}

cola_espera = []
camiones_atendidos = []

tiempo = 0
tiempo_llegada_proximo_camion = get_tiempo_llegada_proximo_camion()

if __name__ == "__main__":

    for i in range(1000):

        if tiempo == tiempo_llegada_proximo_camion:
            print(f"Camion llega a las {tiempo}")
            cola_espera.append({"tiempo_llegada": tiempo})
            tiempo_llegada_proximo_camion = get_tiempo_llegada_proximo_camion()
            mostrar_estado_surtidores()
            


        alguno_libre = verificar_ocupacion_surtidores()

        if alguno_libre and len(cola_espera) > 0:
            camion = cola_espera.pop(0)
            surtidor = elegir_surtidor()
            ocupar_surtidor(surtidor)
            print(f"Camion atendido en surtidor {surtidor} a las {tiempo}, esperó durante {tiempo - camion['tiempo_llegada']} minutos")
            mostrar_estado_surtidores()
            camiones_atendidos.append(
                {
                    "tiempo_llegada": camion["tiempo_llegada"],
                    "tiempo_atencion": tiempo,
                    "surtidor": surtidor,
                }
            )

        tiempo += 1

    generar_grafico_tiempo_espera()
