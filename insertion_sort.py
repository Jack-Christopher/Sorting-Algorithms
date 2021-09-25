def insertion_sort(arreglo):
    for i in range(1, len(arreglo)):
        j = i
        while j > 0 and arreglo[j] < arreglo[j-1]:
            arreglo[j], arreglo[j-1] = arreglo[j-1], arreglo[j]
            j -= 1
    return arreglo


lista = [int(x) for x in input().split()]
print(insertion_sort(lista))