def merge_sort(arreglo, inicio, fin):
    if inicio < fin:
        mitad = (inicio + fin) // 2
        merge_sort(arreglo, inicio, mitad)
        merge_sort(arreglo, mitad + 1, fin)
        merge(arreglo, inicio, mitad, fin)

def merge(arreglo, inicio, mitad, fin):
    izq = inicio
    der = mitad + 1
    aux = []
    while izq <= mitad and der <= fin:
        if arreglo[izq] < arreglo[der]:
            aux.append(arreglo[izq])
            izq += 1
        else:
            aux.append(arreglo[der])
            der += 1
    while izq <= mitad:
        aux.append(arreglo[izq])
        izq += 1
    while der <= fin:
        aux.append(arreglo[der])
        der += 1
    for i in range(len(aux)):
        arreglo[inicio + i] = aux[i]

lista = [int(x) for x in input().split()]
merge_sort(lista, 0, len(lista) - 1)
print(lista)



