def binary_search(num, left, right, x):
    if right >= left:

        mid = left + (right-left)//2

        if num[mid] == x:
            return mid
        elif num[mid]>x:
            return  binary_search(num,left, mid-1, x)
        else:
            return  binary_search(num,mid+1, right, x)

    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
print(binary_search(arr, 0, len(arr)-1, x))

