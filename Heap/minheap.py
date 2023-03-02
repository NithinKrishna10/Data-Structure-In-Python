def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] > arr[left]:
        smallest = left
    if right < n and arr[i] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def insert(array, newnum):
    size = len(array)
    if size == 0:
        array.append(newnum)
    else:
        array.append(newnum)
        for i in range((size // 2) - 1, -1, -1):
            print(i, end="")
            heapify(array, size, i)


def deletenode(array, num):
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


def heapif(arr, size, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[i] > arr[left]:
        smallest = left
    if right < size and arr[i] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]


ar = [4, 5, 10, 15, 2, 23]
print(ar)
arr = []
insert(arr, 4)
insert(arr, 5)
insert(arr, 10)
insert(arr, 15)
insert(arr, 2)
insert(arr, 23)
# heapsort(arr, len(arr))
print("\n", arr)
