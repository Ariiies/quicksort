from quicksort_hirose import quicksort

data = [4,5,9,10,16,1,8,7,2,6,14]
print("Unsorted list")
print(data)
size = len(data)
quicksort(data, 0, size - 1)
print('--- List in ascending sorting ---')
print(data)
quicksort(data, 0, size - 1,True)
print('--- List in descending sorting ---')
print(data)
