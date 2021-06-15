def bubble_sort(num):

    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j+1]<num[j]: # for desc num[j+1]>num[j]
                tmp = num[j]
                num[j] = num[j+1]
                num[j+1] = tmp

    return num


def selection_sort(num):

    for i in range(len(num)-1):
        index = i

        for j in range(i+1, len(num)):
            if num[j]<num[index]:
                index = j
            if index != i:
                tmp = num[i]
                num[i] = num[index]
                num[index] = tmp

    return num

def quick_sort(num,low, high):

    if low >= high:
        return 
    
    pivot = partition(num, low, high)
    quick_sort(num,low, pivot-1)
    quick_sort(num,pivot+1, high)
 
    
def partition(arr, low, high):
    pivot = (low+high)//2
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


if __name__ == "__main__":

    arr = [6,-3,4,88,3,2]
    
    #print(bubble_sort(arr))

    #print(selection_sort(arr))

    print(quick_sort(arr, 0, len(arr)-1))
    print(arr)