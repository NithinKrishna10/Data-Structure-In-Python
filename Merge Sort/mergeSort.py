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

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29]
        # [],
        # [3],
        # [9, 8, 7, 2],
        # [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        # print(arr)

    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    # print(merge_sort1(arr),'gg')
