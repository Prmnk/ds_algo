# basic resursion

def fib(n):
    if n==1 or n==2:
        result =  1
    else:
        result =  fib(n-1) + fib(n-2)
    return result

print(fib(5))


# memoized solution
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


# botton up

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

    
