  
    
# factorial using recursion   
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    

print(factorial(5))

# reverse string using recursion

def reverse_rec(lis, i =0):
    if i != len(lis)-1:
        reverse_rec(lis,i+1)
    print(lis[i])
    

reverse_rec('pramanik')

# fibonacci using recursion

def fibonaci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)

print( fibonaci(6))

print("next")

# power of n using recursion

def power(x,n):
    if n == 0 :
        return 1
    elif n == 1:
        return x
    else:
        return(x*power(x,n-1))

print(power(2,10))
