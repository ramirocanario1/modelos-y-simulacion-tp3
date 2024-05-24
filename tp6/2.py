import numpy as np

def get_demanda_diaria():

    random = np.random.rand()
    
    if random <= 0.2:
        return 25
    elif random <= 0.24:
        return 30
    elif random <= 0.3:
        return 40
    elif random <= 0.42:
        return 50
    elif random <= 0.62:
        return 100
    elif random <= 0.65:
        return 150
    elif random <= 0.8:
        return 200
    elif random <= 0.9:
        return 250
    
    return 300
        
def get_demora_papeleo():
    random = np.random.rand()
    
    if random <= 0.2:
        return 1
    elif random <= 0.5:
        return 2
    elif random <= 0.75:
        return 3
    
    return 4

def get_demora_llegada_producto():
    random = np.random.rand()
    
    if random <= 0.4:
        return 1
    elif random <= 0.6:
        return 2
    elif random <= 0.75:
        return 3
    elif random <= 0.9:
        return 4
    
    return 5

COSTO_MANTENIMIENTO = 450
COSTO_ORDENAR = 3800
COSTO_FALTANTE = 625
COSTO_PRODUCTO = 950

PUNTO_REORDEN = 15

DIAS_SIMULADOS = 365

inventario = 1500
gastos_totales = 0

def registrar_gastos_mantenimiento():
    global gastos_totales
    global inventario

    gastos_totales += COSTO_MANTENIMIENTO * inventario

def ordenar(cantidad=100):
    global inventario
    global gastos_totales
    inventario += cantidad
    gastos_totales += COSTO_ORDENAR + COSTO_PRODUCTO * cantidad

def retirar(cantidad):
    global inventario
    global gastos_totales

    if cantidad > inventario:
        costo_por_faltantes = COSTO_FALTANTE * (cantidad - inventario)
        gastos_totales += costo_por_faltantes
        print(f"No se han podido vender {cantidad - inventario} productos por falta de stock (${costo_por_faltantes})")
        inventario = 0
    else: 
        print(f"Se han vendido {cantidad} productos, quedan {inventario - cantidad} en stock")
        inventario -= cantidad

if __name__ == '__main__':

    for i in range(DIAS_SIMULADOS):
        demanda = get_demanda_diaria()
        retirar(demanda)

        if inventario <= PUNTO_REORDEN:
            ordenar()

        registrar_gastos_mantenimiento()

    print(f"Se han simulado {DIAS_SIMULADOS} días")
    print(f"Gastos totales: {gastos_totales}")
        
