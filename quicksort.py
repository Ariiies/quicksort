# function for the partition of the array
# in this case, sublist are used, them the original list 
# is no modficated, is easy to understad but consume more 
# recurses than other options
def partition(array):
    # the pivot can be other number, but the first one works well
    pivot, high, low = array[0], [], []
    # here is  when the original array is divided
    for i in range(1,len(array)):
        if pivot > array[i]:
            low.append(array[i])
        else:
            high.append(array[i])
        # the three arrays are returned
    return low, pivot, high
# main function 
def quicksort(array, reverse=False):
    # base case to sign the end of the recursive loop
    if len(array)<2:
        return array
    # here are asignated the values
    high, pivot, low = partition(array)
    # for descending sorting 
    if reverse: 
        return quicksort(low, True) + [pivot] + quicksort(high, True)
    # for an ascending sorting
    else: 
        return quicksort(high, False) + [pivot] + quicksort(low, False)

