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


matrix = [[3,7,8],[9,11,13],[15,16,17]]  

res = [min(i) for i in matrix]

res2 = [max(i) for i in matrix]

print(res)
print(res2)

       
            
                
