from heapq import heappop, heappush, heapify

heap= []
nums = [12,-1,4,5,7,2,10]

for num in nums:
    heappush(heap,num)

#min-heap by defualt 

while heap:
    print(heappop(heap))

heapify(nums)

print(nums)


def binary_search(arr, l, r , x):
    if r>= l:
        mid = l + (r-l)//2

        if arr[mid] ==x:
            return mid

        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)

        else:
            return binary_search(arr,mid+1,r,x)

    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

print(binary_search(arr, 0, len(arr)-1, x))

from heapq import heappop, heappush, heapify

def findKthLargest(self, nums, k: int) -> int:
    
    #initialize heap
    
    heap_num = []
    
    for i in nums:
        heappush(heap_num, -i) # -i for max heap
        
    
    while k :
        if k ==1:
            return -1 * heappop(heap_num)
        heappop(heap_num)
        k -=1