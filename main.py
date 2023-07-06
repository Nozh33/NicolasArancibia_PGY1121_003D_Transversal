import numpy as np
from Funciones import *
from Asistente import *

arreglo_asistente = np.full((10, 10), '---')
lista_asistente = []
ciclo = True

llenarArreglo(arreglo_asistente)
#mostrarArreglo(arreglo_asistente)

def validarRut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if str(rut).isdigit and len(str(rut)) == 8:
                return rut
            else:
                print("Rut debe ser de 8 digitos")
        except BaseException as error:
            print(f"error:{error}")

def ingresarAsistente(lista_asistente, num_asiento):
    asistente = Asistente()
    asistente.rut = validarRut()
    asistente.nombre = input("Ingrese nombre del asistente: ")
    asistente.num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <= 20:
        asistente.valor = 120000
    if num_asiento >= 21 and num_asiento <= 50:
        asistente.valor = 80000
    if num_asiento >= 51 and num_asiento <= 100:
        asistente.valor = 50000
    print("Entrada comprada con exito")
    lista_asistente.append(asistente)
def comprarEntrada(arreglo_asistente, lista_asistente):
    compra = 0
    try:
        cantidad = int(input("Ingrese cantidad de entradas: "))
        if cantidad >= 1 and cantidad<= 3:
            while compra < cantidad:
                mostrarArreglo(arreglo_asistente)
                try:
                    num_asiento = int(input("Seleccione numero de asiento: "))
                    if num_asiento >= 1 and num_asiento <= 100:
                        respuesta = verificarAsiento(arreglo_asistente, num_asiento)
                        if respuesta == True:
                            marcarAsiento(arreglo_asistente, num_asiento)
                            ingresarAsistente(lista_asistente, num_asiento)
                            compra = compra + 1
                        else:
                            print("Asiento no disponible")
                except BaseException as error:
                    print(f"error: {error}")
        else:
            print("Cantidad debe ser entre 1 y 3")

    except BaseException as error:
        print(f"error:{error}")

def listadoAsistentes(lista_asistente):
    print("LISTADO DE ASISTENTES:")
    print("---------------------")
    for asistente in lista_asistente:
        print(f"Rut: {asistente.rut}\tNombre: {asistente.nombre}")

def gananciasTotales(lista_asistente):
    print("GANANCIAS TOTALES")
    print("-----------------")
    platinum = 0
    gold = 0
    silver = 0
    for asistente in lista_asistente:
        if int(asistente.valor) == 120000:
            platinum = platinum + 1
        if int(asistente.valor) == 80000:
            gold = gold + 1
        if int(asistente.valor) == 50000:
            silver = silver + 1
    print("Tipo Entrada\tCantidad\tTotal")
    print(f"Platinum: \t\t{platinum}\t\t\t${platinum * 120000}")
    print(f"Gold: \t\t\t{gold}\t\t\t${gold * 80000}")
    print(f"Silver:\t\t\t{silver}\t\t\t${silver * 50000}")
    total_entradas = platinum + gold + silver
    total_valor = (platinum*120000) + (gold*80000) + (silver*50000)
    print(f"TOTAL: \t\t\t{total_entradas}\t\t\t${total_valor}")


while ciclo:
    print("Productora Creativos.cl")
    print("1- Comprar Entradas")
    print("2- Mostrar ubicaciones disponibles")
    print("3- Ver listado de asistentes")
    print("4- Mostrar ganancias totales")
    print("5- Salir")
    try:
        op = int(input("Seleccione (1-5): "))
        match op:
            case 1:
                comprarEntrada(arreglo_asistente, lista_asistente)
            case 2:
                mostrarArreglo(arreglo_asistente)
            case 3:
                listadoAsistentes(lista_asistente)
            case 4:
                gananciasTotales(lista_asistente)
            case 5:
                ciclo = salir()
            case _:
                print("Seleccion invalida")
    except BaseException as error:
        print(f"error: {error}")




