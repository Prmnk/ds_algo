arr1 = [1,2,3,4]
arr2 = [24,12,8,6]

def productExceptSelf( nums):
    nums_l, nums_r = [1] * len(nums), [1] * len(nums)

    res = []

    for i in range(1,len(nums)):
        nums_l[i]  = nums_l[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        nums_r[i] = nums_r[i+1] * nums[i+1]

    for i in range(len(nums)):
        res.append(nums_l[i]*nums_r[i]) 

    
    
    return res    

print(productExceptSelf(arr1))

def firstMissingPositive( nums):
    
    le = len(nums)
    res =[]
    for i in range(le):
        if nums[i] > 0 :
            res.append(nums[i])
    print(res)       
    res.sort()
    print(res)
    if res[0] != 1:
        return 1
    
    for j in range(len(res)-1):   
        print (res[j]+1,res[j+1] )         
        if res[j] !=  res[j+1]  and res[j]+1 < res[j+1]:
            print (res[j]+1,res[j+1] )
            return res[j] + 1


    if res[-1] == len(res):
        return res[-1]+1

def findDisappearedNumbers( nums):
    nums = sorted(nums)
    v, j, i = [], 1, 0
    while i < len(nums):
        if nums[i] == j:
            j += 1
            i += 1
        elif nums[i] < j:
            i += 1
        elif nums[i] > j:
            v.append(j)
            j += 1
    if len(nums) > nums[-1]:
        for i in range(nums[-1]+1, len(nums)+1):
            v.append(i)
    return v

print(firstMissingPositive([1,3,3]))

from collections import defaultdict
class Solution:
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

#floyd cycle detection

def detectCycle( head):
    slow = fast = node = head
    
    # Figure out if there's a cycle and first-intersection
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: break
    else:
        return None
    
    # Find cycle entrance
    while node is not slow:
        node, slow = node.next, slow.next
    return node