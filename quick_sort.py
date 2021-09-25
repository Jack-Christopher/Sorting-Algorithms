def quick_sort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivote = arreglo[0]
        menores = [x for x in arreglo[1:] if x <= pivote]
        mayores = [x for x in arreglo[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)


lista = [int(x) for x in input().split()]
print(quick_sort(lista))