def heap_sort (arreglo):
    n = len(arreglo)
    for i in range(n, -1, -1):
        heapify(arreglo, n, i)
    for i in range(n-1, 0, -1):
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
        heapify(arreglo, i, 0)
    return arreglo


def heapify(arreglo, n, i):
    mayor = i
    izq = 2*i + 1
    der = 2*i + 2
    if izq < n and arreglo[izq] > arreglo[mayor]:
        mayor = izq
    if der < n and arreglo[der] > arreglo[mayor]:
        mayor = der
    if mayor != i:
        arreglo[i], arreglo[mayor] = arreglo[mayor], arreglo[i]
        heapify(arreglo, n, mayor)

lista = [int(x) for x in input().split()]
print(heap_sort(lista))
    