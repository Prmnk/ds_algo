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

def maxRepeating(sequence: str, word: str) -> int:
    le_word = len(word)
    le_seq = len(sequence)
    cnt, i = 0,0
    
    if word == sequence:
        return 1
    while i < le_seq:
        print(i)
        if sequence[i:i+le_word] == word:
            cnt +=1
            i += le_word
            print(str(cnt), word)
            print(i)
        else:
            i += 1
            
    return cnt

print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))


def maxSubArray( nums):
	if len(nums)==1:
		return nums[0]
	arr=[]
	s=0
	flag=1 #To check if in nums all are -ve, If all -ve then flag=1
	for i in range(len(nums)):
		s=s+nums[i]
		if nums[i]>0:
			flag=0
		if s<0:   # It will make sum zero whenever sum is going -ve
			s=0  
		arr.append(s)
	if flag==1: # Handling when nums array consists of all -ve integers
		return max(nums)
	return max(arr)

def findShortestSubArray(nums) :
    
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left: left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1
           
    ans = len(nums)
    degree = max(count.values())
    
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x]- left[x] + 1)
            
    return ans

def maxProfit( prices, fee) :
    
    max_profit = 0
    min_price = prices[0]
    
    for i in range(len(prices)):
        
        if prices[i]< min_price:
            min_price = prices[i]
        elif prices[i] > min_price + fee:
            max_profit += (prices[i]- min_price -fee)
            min_price = prices[i] - fee
        
            
    return max_profit


for i, c in enumerate('bdbdbd'):
    print (i,c)

from collections import defaultdict

def longestPalindrome(self, s: str) -> int:
    res = 0
    hash_t = defaultdict(int)
    
    for i in s:
        hash_t[i] +=1 
        
    
    if len(s)==1:
        return 1
    elif len(s) ==2 and len(hash_t.keys()) ==2:
        return 1
    else:
        for j in hash_t.keys():
            res += hash_t[j]//2 * 2
            if res%2 == 0 and hash_t[j] %2 ==1 :
                res += 1
    
        
    return res

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')



#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1011974/BFS-two-pointers-and-recursive
def findTarget(root, k) -> bool:
    queue = [root]
    unique_set = set()
    
    while len(queue) > 0:
        current = queue.pop()
        if k - current.val in unique_set: return True
        unique_set.add(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    
    return False


# find if linkedlist is palindrome with o(N) time and o(1) space
'''
def isPalindrome( head) -> bool:
    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    prev=None
    curr=slow
    while(curr):
        nextt=curr.next
        curr.next=prev
        prev=curr
        curr=nextt
    
    while(prev):
        if(prev.val!=head.val):
            return False
        prev=prev.next
        head=head.next
    return True
'''
def thirdMax( nums) :
    
    max_1 = nums[0]
    max_2 = float('-inf')
    max_3 = float('-inf')

    if len(nums)<3:
        return (max(nums))
    
    for i in range(len(nums)):
        
        if nums[i] > max_1 :
            max_3 = max_2
            max_2 = max_1            
            max_1 = nums[i]
            
        elif nums[i] < max_1 and nums[i] > max_2 :
            max_3 = max_2
            max_2 = nums[i]
            
        elif nums[i] < max_2 and nums[i] > max_3 :
            max_3 = nums[i]

        print (nums[i], max_3, max_2, max_1)
            

   
    return max_3  if max_3 != float('-inf') else max_1

print(thirdMax([1,2,-2147483648]))

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

