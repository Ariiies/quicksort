# particion para el ordenamiento, este altera la lista
# orginal, su logica es mas compleja pero consume menos
# recursos
def partition(array, low, high, reverse=False):
    # elegimos el primer elemento
    pivot, le, ri = array[low], low+1, high
    # buvle principal donde se divide la lista
    while True:
        if reverse: # para un ordenamiento descendente
            while le <= ri and array[le] >= pivot:
                le+=1
            while le <= ri and array[ri] <= pivot:
                ri-=1
        else: # para un ordenamiento ascendente
            while le <= ri and array[le] <= pivot:
                le+=1
            while le <= ri and array[ri] >= pivot:
                ri-=1
        if ri < le:
            break
        else:
            array[le], array[ri] = array[ri], array[le]
    array[low], array[ri] = array[ri], array[low]
    return ri

# funsion de ordenamiento quicksort
def quicksort(array, low, high, reverse=False):
    if low < high:
        pi = partition(array, low, high,reverse)
        quicksort(array, low, pi - 1,reverse)
        quicksort(array, pi + 1, high,reverse)

