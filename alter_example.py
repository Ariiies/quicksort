from quicksort_hirose import quicksort

data = [4,5,9,10,16,1,8,7,2,6,14]
print("Unsorted list")
print(data)
size = len(data)
quicksort(data, 0, size - 1)
print('Sorted list in ascending order:')
print(data)
quicksort(data, 0, size - 1,True)
print('Sorted list in descending order:')
print(data)
