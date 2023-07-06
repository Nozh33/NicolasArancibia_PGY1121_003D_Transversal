def llenarArreglo(arreglo_asistente):
    x = 1
    for f in range(10):
        for c in range(10):
            if len(str(x)) == 1:
                arreglo_asistente[f][c] = '00' + str(x)
            if len(str(x)) == 2:
                arreglo_asistente[f][c] = '0' + str(x)
            if len(str(x)) == 3:
                arreglo_asistente[f][c] = str(x)
            x = x + 1

def marcarAsiento(arreglo_asistentes, num_asiento):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_asiento:
                arreglo_asistentes[f][c] = 'XXX'
            x = x + 1

def verificarAsiento(arreglo_asistente, num_asiento):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_asiento:
                if arreglo_asistente[f][c] == 'XXX':
                    return False
            x = x + 1
    return True

def mostrarArreglo(arreglo_asistente):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' | ' + arreglo_asistente[f][c]
        print(fila)

def salir():
    print("Nicolas Arancibia 06-07-2023")
    return False