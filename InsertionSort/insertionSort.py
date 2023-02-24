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
        while pos >0 and arr[pos]>key:
            arr[pos+1] = arr[pos]
            pos -= 1
        arr[pos+1] = key



def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key
        print(array)
    return array




if __name__ == '__main__':
    array = [30, 3, 41, 56, 12, 11, 8]
    # print(insort(array))
    # print(selection(array))
    # merge(array)
    size = len(array)
    # quick(array,0,size)
    # print(array)
    print(insertionSort(array))

