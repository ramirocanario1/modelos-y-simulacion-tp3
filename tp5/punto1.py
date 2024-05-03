from random import randint

def confidence_interval(n_sample, mean, std, z_value=2.57, coeff=1.):
    z_term = coeff * (z_value * std / (n_sample ** 0.5))
    inf = mean - z_term
    sup = mean + z_term
    return (inf, sup)
 
tareas =  {
    'A': {'nombre': 'Romper huevos', 'demora': (2, 4)},
    'B': {'nombre': 'Revolver huevos', 'demora': (3, 6)},
    'C': {'nombre': 'Cocinar huevos', 'demora': (2, 5)},
    'D': {'nombre': 'Cortar panes', 'demora': (3, 6)},
    'E': {'nombre': 'Preparar tostadas', 'demora': (2, 5)},
    'F': {'nombre': 'Preparar bebidas calientes (te, cafe)', 'demora': (4, 8)},
    'G': {'nombre': 'Preparar bebidas frias (jugos, yogur)', 'demora': (3, 7)}
}

def calcular_demora(tarea):
    min = tarea['demora'][0]
    max = tarea['demora'][1]
    return randint(min, max)

def realizar_tarea(id):
    tarea = tareas[id]
    # print(f"Realizando tarea {tarea['nombre']}...")
    demora = calcular_demora(tarea)
    return demora

def realizar_experimento():
    tiempos = {
        'acceso_superior': [],
        'acceso_medio': [],
        'acceso_inferior': [],
        'tiempos_totales': [],
    }

    # For de 100 iteraciones
    for i in range(100):

        tiempo_acceso_superior = 0
        tiempo_acceso_superior += realizar_tarea('A')
        tiempo_acceso_superior += realizar_tarea('B')
        tiempo_acceso_superior += realizar_tarea('C')
        tiempos['acceso_superior'].append(tiempo_acceso_superior)

        tiempo_acceso_medio = 0
        tiempo_acceso_medio += realizar_tarea('D')
        tiempo_acceso_medio += realizar_tarea('E')
        tiempos['acceso_medio'].append(tiempo_acceso_medio)

        tiempo_acceso_inferior = 0
        tiempo_acceso_inferior += realizar_tarea('F')
        tiempo_acceso_inferior += realizar_tarea('G')
        tiempos['acceso_inferior'].append(tiempo_acceso_inferior)

        tiempo_total = max(tiempo_acceso_superior, tiempo_acceso_medio, tiempo_acceso_inferior)
        tiempos['tiempos_totales'].append(tiempo_total)
    
    promedio_acceso_superior = sum(tiempos['acceso_superior']) / len(tiempos['acceso_superior'])
    promedio_acceso_medio = sum(tiempos['acceso_medio']) / len(tiempos['acceso_medio'])
    promedio_acceso_inferior = sum(tiempos['acceso_inferior']) / len(tiempos['acceso_inferior'])
    promedio_tiempos_totales = sum(tiempos['tiempos_totales']) / len(tiempos['tiempos_totales'])

    return (promedio_acceso_superior, promedio_acceso_medio, promedio_acceso_inferior, promedio_tiempos_totales)

def calcular_mayor_criticidad(tiempos):

    superior = tiempos['acceso_superior']
    medio = tiempos['acceso_medio']
    inferior = tiempos['acceso_inferior']
    res = []

    for i in range(len(superior)):
        if superior[i] > medio[i] and superior[i] > inferior[i]:
            res.append('superior')
        elif medio[i] > superior[i] and medio[i] > inferior[i]:
            res.append('medio')
        else:
            res.append('inferior')

    # Obtener la cantidad de ocurrencias de cada uno
    superior_count = res.count('superior')
    medio_count = res.count('medio')
    inferior_count = res.count('inferior')

    # Retornar el de mayor cantidad
    if superior_count > medio_count and superior_count > inferior_count:
        return 'superior'
    elif medio_count > superior_count and medio_count > inferior_count:
        return 'medio'
    else:
        return 'inferior'

if __name__ == '__main__':

    tiempos = {
        'acceso_superior': [],
        'acceso_medio': [],
        'acceso_inferior': [],
        'tiempos_totales': [],
    }

    for i in range(30):
        (promedio_acceso_superior, 
         promedio_acceso_medio, 
         promedio_acceso_inferior, 
         promedio_tiempos_totales) = realizar_experimento()
        
        tiempos['acceso_superior'].append(promedio_acceso_superior)
        tiempos['acceso_medio'].append(promedio_acceso_medio)
        tiempos['acceso_inferior'].append(promedio_acceso_inferior)
        tiempos['tiempos_totales'].append(promedio_tiempos_totales)

    promedio_tiempos_totales = round(sum(tiempos['tiempos_totales']) / len(tiempos['tiempos_totales']), 2)

    print(f"Promedio de tiempo total: {promedio_tiempos_totales}")

    inf, sup = confidence_interval(30, promedio_tiempos_totales, 1.5)
    print(f"Intervalo de confianza: ({inf}, {sup})")

    mayor_criticidad = calcular_mayor_criticidad(tiempos)
    print(f"El acceso de mayor criticidad es el {mayor_criticidad}")
    

    