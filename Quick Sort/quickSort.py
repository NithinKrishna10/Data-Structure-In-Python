# to get the correct position of the pivot element
def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    print(list1[right], "Right", right, "left", list1[left], "l", left)
    print("list", "==================================================", list1, "===================================")
    list1[first], list1[right] = list1[right], list1[first]
    print(list1[right], "Right", right, "left", list1[left], "l", left)
    print("list", "==================================================", list1, "===================================")
    return right


def quicksort(list1, first, last):
    print("first", first, "last", last)
    if first < last:
        p = pivot_place(list1, first, last)
        quicksort(list1, first, p - 1)
        quicksort(list1, p + 1, last)


# main
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def swap(arr,l,m):
    if l !=m:
        arr[l],arr[m]= arr[m],arr[l]


def pivotd(list,first,last):
    pivot_index = first
    pivot = list[pivot_index]
    while first<last:
        if first < len(list) and list[first] <= pivot:
            first +=1
        if list[last]> pivot:
            last -= 1
        if first < last:
            swap(list,first,last)
    swap(list,pivot_index,last)
    return last


def pivoting(list,start,end):
    pindex = start
    pelm = list[pindex]

    while start<end:
        if start < len(list) and list[start]<= pelm:
            start +=1
        if list[end]>pelm:
            end -=1
        if start<end:
            swap(list,start,end)
    swap(list,pindex,end)

    return end



def quicker(element, start, end):
    if start < end:
        pi = pivoting(element, start, end)
        quicker(element, start, pi - 1)
        quicker(element, end, pi+1)


if __name__ == '__main__':
    list = [12, 45, 32, 21, 5, 2]
    quicker(list, 0, len(list)-1)
    print(list)


# if __name__ == '__main__':
#     list1 = [56, 26, 93, 17, 31, 44]
#     # list1 = [8, 6, 15, 4, 33, 2]
#     n = len(list1)
#     quicksort(list1, 0, n - 1)
#     print(list1)
#     my_list = [5, 2, 8, 1, 9, 4]
#     # sorted_list = quick_sort(my_list)
#     # print("quick", sorted_list)  # Output: [1, 2, 4, 5, 8, 9]
