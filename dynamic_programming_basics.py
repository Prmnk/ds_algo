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
print(max_tasks(high, low, n))
print(max_task_dp(high, low, n))


