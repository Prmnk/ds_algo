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
