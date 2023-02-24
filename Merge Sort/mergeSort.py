# def merge_sort1(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     return merge_two_sorted_lists1(left, right, arr)
#
#
# def merge_two_sorted_lists1(a, b, arr):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)
#     i = j = k = 0
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             k += 1
#             i += 1
#         else:
#             sorted_list.append(a[j])
#             k += 1
#             j += 1
#
#     while i < len_a:
#         arr[k] = a[i]
#         i += 1
#         k += 1
#     while j < len_b:
#         arr[k] = a[j]
#         j += 1
#         k += 1
#     return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2

    right = arr[mid:]
    left = arr[:mid]
    print('left =',left,"     right =",right)

    merge_sort(left)
    merge_sort(right)
    print("\n",arr,"array\n")
    merge_two_sorted_lists(left, right, arr)
def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    print("###############################################",arr,"##################################################")


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def merge(arr):
    if len(arr)>1:

        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]
        merge(l)
        merge(r)

        i=j=k=0

        while i < len(l) and j < len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1


        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1



def meger(arr):
    if len(arr)>1:
        mid = len(arr)//2
        f = arr[:mid]
        l = arr[mid:]
        meger(f)
        meger(l)
        i=j=k=0
        while i < len(f) and j <len(l):
            if f[i]<l[j]:
                arr[k] = f[i]
                i +=1
            else:
                arr[k] = l[j]
                j += 1
            k += 1
        while i<len(f):
            arr[k] = f[i]
            i +=1
            k +=1
        while j<len(l):
            arr[k] = l[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge(arr)
        print(arr)

    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    # print(merge_sort1(arr),'gg')
