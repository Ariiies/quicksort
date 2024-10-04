# Function to partition, it works in the same list, is a litle more 
# difficult to understand but it consumes less resources 
def partition(array, low, high, reverse=False):
    # dwfinition of pivot and pointiers 
    pivot, le, ri = array[low], low+1, high
    while True:
        # reverse is for sorting list in ascending or descending
        # move the pointiers...
        if reverse: 
            while le <= ri and array[le] >= pivot:
                le+=1
            while le <= ri and array[ri] <= pivot:
                ri-=1
        else: 
            while le <= ri and array[le] <= pivot:
                le+=1
            while le <= ri and array[ri] >= pivot:
                ri-=1
        if ri < le: # when pointiers crossing it each other, breaks the loop
            break
        else:
            array[le], array[ri] = array[ri], array[le]
    array[low], array[ri] = array[ri], array[low]
    return ri #returns ri because this will be the new pivot

# main function
def quicksort(array, low, high, reverse=False):
    if low < high:
        pi = partition(array, low, high,reverse)
        quicksort(array, low, pi - 1,reverse)
        quicksort(array, pi + 1, high,reverse)

