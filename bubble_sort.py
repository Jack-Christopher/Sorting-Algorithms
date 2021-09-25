def bubble_sort(arreglo):
    for i in range(len(arreglo)):
        for j in range(len(arreglo)-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

lista = [int(x) for x in input().split()]
print(bubble_sort(lista))