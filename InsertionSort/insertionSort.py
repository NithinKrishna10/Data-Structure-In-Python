# def insertionSort(array):
#     for i in range(1, len(array)):
#         current = array[i]
#         j = i - 1
#         while j >= 0 and array[j] > current:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = current
#     return array

def insort(arr):
    for i in range(len(arr)):
        key = arr[i]
        pos = i -1
        while i >0 and arr[pos]>key:
            arr[pos+1] = arr[pos]
            pos -= 1
        arr[pos+1] = key
if __name__ == '__main__':
    array = [30, 3, 41, 56, 12, 11, 8]
    # print(insertionSort(array))

