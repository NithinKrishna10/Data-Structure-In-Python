# Max-Heap
def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[i] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def insert(array, newnode):
    size = len(array)
    if size == 0:
        array.append(newnode)
    else:
        array.append(newnode)
        for i in range((size // 2) - 1, -1, -1):
            heapify(arr, size, i)


def delete(array, num):
    size = len(array)
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size - 1] = array[size - 1], array[i]
    array.remove(num)
    for i in range((size // 2) - 1, -1, -1):
        heapify(array, len(array), i)


def heapsort(arr, size):
    for i in range((size // 2) - 1, -1, -1):
        heapify(arr, size, i)
    for i in range(size - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapsorts(arr,size):
    for i in range((size // 2)-1,-1,-1):
        heapify(arr,size,i)
    for i in range(size-1,-1,-1):
        arr[0],arr[i]= arr[i],arr[0]
        heapify(arr,i,0)

arr = []
insert(arr, 1)
insert(arr, 3)
insert(arr, 36)
insert(arr, 73)
insert(arr, 21)
insert(arr, 12)
insert(arr, 43)
insert(arr, 25)
print("Max Heap      :", str(arr))
delete(arr, 12)
# arr.sort()
heapsorts(arr, len(arr))
print("\nAfter deletion:", str(arr))
