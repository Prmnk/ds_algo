n= [5,1,6]


import functools
import itertools

def superdig(n):
    sum = 0 

    def super_dig_rec(arr,idx,tot):
        if idx == len(arr)-1:
            return tot
        
        for i in range(len(arr)):
            n = arr[i]
            new_arr = arr[i+1:]
            tot = functools.reduce()
            super_dig_rec(new_arr,)


    return super_dig_rec(n)


def combination_xor(arr):
    res = 0
    for i in range(1, len(arr)+1):
        for arry in itertools.combinations(arr,i):
            su = functools.reduce(lambda x,y: x^y,list(arry))
            res += su
    return res



     


print(combination_xor(n))
       
            
                
