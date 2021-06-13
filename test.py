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






            
                
