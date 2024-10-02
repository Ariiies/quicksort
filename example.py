from quicksort import quicksort
import time
data = [4,5,9,10,16,1,8,7,2,6,14]
print("---Unsorted list---")
print(data)
begin = time.time()
print("---Sorted list in ascending sorting---")
print(quicksort(data))
print("---Sorted list in descending sorting---")
print(quicksort(data, True))
end = time.time()
print("Excecution time: ",end-begin, "s")
