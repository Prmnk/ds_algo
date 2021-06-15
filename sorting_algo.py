def bubble_sort(num):
    # max keeps moving to the end -- bubbles up

    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j+1]<num[j]: # for desc num[j+1]>num[j]
                tmp = num[j]
                num[j] = num[j+1]
                num[j+1] = tmp

    return num


def selection_sort(num):

    # find smallest element then the element in begining of loop
    # swap with element where the loop started with

    for i in range(len(num)-1):
        index = i

        for j in range(i+1, len(num)):
            if num[j] < num[index]:
                index = j

            if index != i:
                tmp = num[i]
                num[i] = num[index]
                num[index] = tmp

    return num

def quick_sort(num,low, high):

    # divide and conquer

    if low >= high:
        return 
    
    pivot = partition(num, low, high)
    
    quick_sort(num,low, pivot-1)
    quick_sort(num,pivot+1, high)
 
    
def partition(arr, low, high):
    pivot = (low+high)//2
    # swap high with pivot    
    tmp = arr[high]
    arr[high] = arr[pivot]
    arr[pivot] = tmp
    
    i = low

    for j in range(low, high):
        if arr[j]<=arr[high]: # arr[j] > arr[high] for descending order
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1

    tmp = arr[i]
    arr[i] = arr[high]
    arr[high] = tmp
 

    return i


def merge_sort(arr):
    # divide and conquer
    # divide the array until all array with one element
    # merge all of the them one by one by arranging

    if len(arr)==1: return

    middle = len(arr)//2

    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def insertion_sort(arr):

    # in place ,start from begining, keep inserting smaller items in the back at right place

    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1]>arr[j] :
            tmp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = tmp
            j -= 1

    return arr



if __name__ == "__main__":

    arr = [6,-3,4,88,3,2]
    
    #print(bubble_sort(arr))

    #print(selection_sort(arr))

    print(quick_sort(arr, 0, len(arr)-1))

    #print(merge_sort(arr))

    #print(insertion_sort(arr))
    print(arr)