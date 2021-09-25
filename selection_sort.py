def selection_sort(arreglo):
    for i in range(len(arreglo)):
        min = i
        for j in range(i+1, len(arreglo)):
            if arreglo[j] < arreglo[min]:
                min = j
        arreglo[i], arreglo[min] = arreglo[min], arreglo[i]
    return arreglo

lista = [int(x) for x in input().split()]
print(selection_sort(lista))