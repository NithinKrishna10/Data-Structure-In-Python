def bubble_sort(array):
    size = len(array) - 1
    for i in range(size):
        swapped = False
        for j in range(size - i):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                swapped = True
        if not swapped:
            break


# def bubble_sort1(array, key=None):
#     size = len(array) - 1
#     for i in range(size):
#         swapped = False
#         for j in range(size - i):
#             a = elements[j][key]
#             b = elements[j + 1][key]
#             if a > b:
#                 tmp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = tmp
#                 swapped = True
#         if not swapped:
#             break


def bubble(arr):
    size = len(arr)-1
    for i in range(size):
        for j in range(size-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__ == '__main__':
    # elements = [
    #     {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    #     {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #     {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    #     {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    # ]
    arr = [8, 5, 4, 465, 67, 7, 84, 3, 9]

    # bubble_sort(arr)
    # bubble_sort1(elements, key='transaction_amount')
    # print(arr)
    # for i in elements:
    #     print(i)
    # bubble_sort1(elements,key='name')
    # print()
    # for i in elements:
    #     print(i)
    bubble(arr)
    print(arr)