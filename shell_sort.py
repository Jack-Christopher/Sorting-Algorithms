def shell_sort(arreglo):
    gap = len(arreglo) // 2
    while gap > 0:
        for posicion_inicial in range(gap):
            gap_insertion_sort(arreglo, posicion_inicial, gap)
        gap = gap // 2
    
    return arreglo

def gap_insertion_sort(arreglo, inicio, gap):
    for i in range(inicio + gap, len(arreglo), gap):
        valor_actual = arreglo[i]
        posicion = i
        while posicion >= gap and arreglo[posicion - gap] > valor_actual:
            arreglo[posicion] = arreglo[posicion - gap]
            posicion = posicion - gap
        arreglo[posicion] = valor_actual

lista = [int(x) for x in input().split()]
print(shell_sort(lista))