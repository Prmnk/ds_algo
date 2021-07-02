n= [5,1,6]


import functools
import itertools


def combination_xor(arr):
    res = 0
    for i in range(1, len(arr)+1):
        for arry in itertools.combinations(arr,i):
            su = functools.reduce(lambda x,y: x^y,list(arry))
            res += su
    return res


def subsetXORSum(self, nums):
  res = 0
  def subsets(i=0, path=0):
    nonlocal res
    if i == len(nums):
      res += path
      return
    
    subsets(i + 1, path ^ nums[i])
    subsets(i + 1, path)
  
  subsets()
  return res



def luckyNumbers ( matrix):
        
        res =[]
        
        lis_min = []
        lis_max = [0] * len(matrix[0])
        
        for y in range(len(matrix)):
            lis_min.append(min(matrix[y]))   
            
            for x in range(len(matrix[y])):
                if matrix[y][x]>lis_max[x]:
                    lis_max[x] =  matrix[y][x]
                    
        print (lis_max,lis_min)
                    
        for i in range (len(lis_min)):
            if lis_min[i] in lis_max:
                res.append(lis_min[i])
                
        return res

#print(luckyNumbers([[56216],[63251],[75772],[1945],[27014]])   )  
#print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])   )  


def shortestToChar( s: str, c: str):
    pos_c =[]
    le = len(s)
    res=[0] * le
    for i in range(le):
        if s[i]==c:
            pos_c.append(i)
            
    for i in range(le):
        for j in range(len(pos_c)):
            if abs(i-pos_c[j]) <= res[i] or j == 0 :
                res[i] = abs(i-pos_c[j])
                
    return res


def prime(n):
    res =[]

    if n<2:
        return res

    if n==2:
        res.append(2)
        return res

    res.append(2)

    for i in range(3,n,2):
        cnt = 0
        for j in range(1,int(i//2)+1):
            if i%j ==0 : cnt+=1

        if cnt==1: res.append(i)

    return res

print(prime(20))


# recognise palindrome 

def isPalindrome(self, s: str) -> bool:
    
    if len(s)<2:
        return True
    
    left = 0
    right = len(s)-1        
    
    while left < right:       
        
        while left < right and not (s[left].isdigit() or s[left].isalpha()):
            left +=1
        while left < right and not (s[right].isdigit() or s[right].isalpha()):
            right -=1           
        
        if s[right].isalpha() and s[left].isalpha() and s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        elif  s[right].isdigit() and s[left].isdigit() and s[left] == s[right]:
            left += 1
            right -= 1
        elif left >= right:
            return True
        else:
            #print (left,right,s[left], s[right],len(s))
            return False
        
    return True
        
        
def breakPalindrome(self, palindrome: str) -> str:
    le = len(palindrome)
    src = 'abcdefghijklmnopqrstuvwxyz'
    pos = ''
    idx = 0
    
    if le < 2:
        return ''
    
    if le%2==0: 
        loop = le/2 
    else: 
        loop = (le-1)/2
    
    
    for i in range(len(src)):
        for j in range(int(loop)):
            if src[i] != palindrome[j]:
                break
            else:
                continue
            break
        else:
            continue
        break
            
    pos = src[i] 
    idx = j
    
    if palindrome[j]=='a':
        idx = le-1-j
    res = palindrome[:idx] + pos + palindrome[idx + 1:]
    
    return res

def minOperations( nums) :
    
    base_diff = nums[0]
    tick = 0
    cnt = 0
    
    for i in range(1,len(nums)):
        curr_diff =  nums[i]-i
        
        if base_diff < curr_diff  :
            base_diff = curr_diff
            tick = 1
        
        cnt = cnt + base_diff - curr_diff

        print (i,nums[i], base_diff, curr_diff, cnt,tick)
        
            
    return cnt
        
                
print(minOperations([6,8,10,1,4,3,9,10,3,2]))


def basic_sort(nums):

    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j+1]<nums[j]:
                tmp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1] = tmp
    
    return nums


print (basic_sort([6,-3,4,88,3,2]))

print (basic_sort(['a','v','b','h','c','z']))



def mostCommonWord( paragraph, banned) -> str:
    dict = {}
    max = 0
    rs = ''
    
    para = ''.join(e for e in paragraph if e.isalnum() or e == ' ')

    print (para)
    
    for i in para.lower().split(" "):
        if i in banned:
            continue
            
        if i in dict.keys():
            dict[i] = dict[i] +1
            if dict[i]>=max: 
                rs = i
                max = dict[i]
        else:
            dict[i] = 1
            if dict[i]>=max: 
                rs = i
                max = dict[i]
    
    return rs


#print(mostCommonWord("a, a, a, a, b,b,b,c, c","a"))



test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using list comprehension
# to remove duplicated 
# from list 
res = []
[res.append(x) for x in test_list if x not in res]

print(res)