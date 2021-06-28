# basic resursion

def fib(n):
    if n==1 or n==2:
        result =  1
    else:
        result =  fib(n-1) + fib(n-2)
    return result

print(fib(5))


# memoized solution -- recursive plus save result to refer to avoid re-calculation
# save results of fib(n) at nth place in an array

def fib_memo(n, memo):
    if memo[n] != None:
        return memo[n]
    if n==1 or n==2:
        result =  1
    else:
        result =  fib(n-1) + fib(n-2)
    memo[n] = result
    return result


print(fib_memo(5, [None] * 6))


# botton up -- 

def fib_bottomup(n):
    if n==1 or n==2:
        return 1
    elif n==0:
        return 0
    bottom_up = [None]*(n+1)
    bottom_up[1]=1
    bottom_up[2] = 1

    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]

print(fib_bottomup(5))

    
# bottom up approach, loop + calculate and store data in an array

def factorial_dp(n):
    f = [0]*(n+1)
    f[0]  = 1
    for i in range(1,n+1):
        f[i] = f[i-1] * i
    return f[n]

#print(factorial_dp(5))

# https://www.geeksforgeeks.org/dynamic-programming-high-effort-vs-low-effort-tasks-problem/

def max_tasks(high, low, n):

    if n <= 0:
        return 0

    return max(high[n-1]+max_tasks(high,low,n-2) , low[n-1]+ max_tasks(high, low, n-1))

def max_task_dp(high, low, n):
    task_dp = [0] *(n+1)
    task_dp[0] = 0
    task_dp[1] = high[0]

    for i in range(2,n+1):
        task_dp[i] = max( high[i-1] +task_dp[i-2], low[i-1]+ task_dp[i-1] )

    return task_dp[n]

n = 5
high = [3, 6, 8, 7, 6]
low = [1, 5, 4, 5, 3]
#print(max_tasks(high, low, n))
#print(max_task_dp(high, low, n))


def climbStairs(self, n: int) -> int:
    d = {}
    if n == 1 : 
        return 1
    
    if n == 2:
        return 2
    
    return climbStairs(n-1) + climbStairs (n-2)

# dp saving the results

def climbStairs(self, n: int) -> int:
    
    self.d = {}
    
    def recur_sol(n):
        if n == 1 : 
            return 1
        
        if n == 2:
            return 2
        
        if n in self.d:
            return self.d[n]
        else:            
            result =  recur_sol(n-1) + recur_sol(n-2)
            self.d[n] = result
        
        return recur_sol(n-1) + recur_sol(n-2)
    
    
    return recur_sol(n)
    

# https://leetcode.com/problems/min-cost-climbing-stairs/
    
def minCostClimbingStairs(cost):
    le = len(cost)
    dp = [0] * (le+1)
    dp[le] = 0
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, le+1):
        if i != le:
            dp[i] = cost[i] + min (dp[i-1] , dp[i-2])
        else:
            dp[i] =  min (dp[i-1] , dp[i-2])
    
    return dp[le]  


def minCostClimbingStairs_recur(cost):
    le = len(cost)
    dp = -1 * [le+1]

    dp[0] = cost[0]
    dp[1] = cost[1]
    def mincost_recur(n):

        if n == 0:
            return dp[0]
        if n == 1:
            return dp[1]
        if dp[n] != -1:
            return dp[n]
        else :
            res =  cost[n] + min(mincost_recur(n-1), mincost_recur(n-2))
            dp[n] = res
        

        return cost[n] + min(mincost_recur(n-1), mincost_recur(n-2))

    return mincost_recur()

cost = [1,100,1,1,1,100,1,1,100,1]  

#https://leetcode.com/problems/n-th-tribonacci-number/submissions/

def tribonacci(self, n: int) -> int:
    if n==1 or n==2:
        return 1
    elif n==0:
        return 0
    dp = [0] * (n +1)
    dp[0], dp[1], dp[2] = 0, 1 , 1

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[n]
 


def generate( numRows: int):
   res = []
   for i in range(numRows):
       row = [None for _ in range(i+1)]
       row[0], row[-1] = 1,1
       
       for j in range(1, len(row)-1):
           row[j] = res[i-1][j-1] + res[j-1][j]
           
       res.append(row)
       
   return res

def isSubsequence( s: str, t: str) :
    
    n = 0
    res = ''
    for i in range(len(s)):
        
        for j in range(n,len(t)):
            if s[i] == t[j]:
                n = j+1
                res += s[i]
                break

    print (res)
    return res==s

s = 'ab'
d = 'baab'

print(isSubsequence(s,d))