def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


if __name__ == '__main__':
    array = [30, 3, 41, 56, 12, 11, 8]
    print(insertionSort(array))

