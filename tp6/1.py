from numpy.random import randn

cantidad_almacenada = 90
costo_total_almacenamiento = 0
turnos_adicionales = 0

CANTIDAD_PRODUCIDA_POR_TURNO = 130
DIAS_LABORALES = 250
AÑOS = 30
DIAS_SIMULADOS = DIAS_LABORALES * AÑOS

CANTIDAD_MINIMA_EN_DEPOSITO = 50

# Funcion para obtener un numero aleatorio normal
def normal(mu, sigma):
    return int(mu + sigma * randn())

def producir(cantidad):
    global cantidad_almacenada
    cantidad_almacenada += cantidad
    return cantidad_almacenada

def retirar(cantidad):
    global cantidad_almacenada
    cantidad_almacenada -= cantidad

    if cantidad_almacenada < 0:
        raise Exception("El almacenamiento no puede ser negativo")

    return cantidad_almacenada

if __name__ == '__main__':

    for i in range(DIAS_SIMULADOS):
        producir(CANTIDAD_PRODUCIDA_POR_TURNO)

        cantidad_demandada_hoy = normal(150, 25)
        # print(f"El demanda actual es {cantidad_demandada_hoy}")
        retirar(cantidad_demandada_hoy)

        if cantidad_almacenada <= CANTIDAD_MINIMA_EN_DEPOSITO:
            producir(CANTIDAD_PRODUCIDA_POR_TURNO)
            turnos_adicionales += 1

        costo_mantenimiento = 70 * cantidad_almacenada
        costo_total_almacenamiento += costo_mantenimiento
    
    print(f"Se han simulado {DIAS_SIMULADOS} días, con una cantidad minima almacenada de {CANTIDAD_MINIMA_EN_DEPOSITO}")
    print(f"Cantidad de turnos adicionales: {turnos_adicionales} ({round(turnos_adicionales / AÑOS, 2)} turnos por año promedio)") 
    print(f"Costo total almacenamiento: {costo_total_almacenamiento} ({int(costo_total_almacenamiento / AÑOS)} costo por año promedio)") 