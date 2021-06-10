
# factorial using recursion   
from typing import List


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

# power of n using recursion

def power(x,n):
    if n == 0 :
        return 1
    elif n == 1:
        return x
    else:
        return(x*power(x,n-1))

print(power(2,10))

# sum of nested list using recursion

def sum_nested(l):
    total = 0
    for i in range(len(l)):
        if type(l[i])==list:
            total += sum_nested(l[i])
        else:
            total += l[i]
    return total

print (sum_nested([[4,5],[7,8,[20]],100]))

#flatten a nested list using recursion

def flat(l):
    output = []
    
    def flatten_list(l):
        for i in l:
            
            if type(i)==list:
                flatten_list(i)
            else:
                
                output.append(i)

    flatten_list(l)

    return output

print (flat([1,[4,5],[7,8,[20]],100]))

# flatten a nested dictionary
def flat_dict(d):
    dict_res = {}
      
    def flatten_dict(d):
        for k, v in d.items():    
            if type(v)==dict:
                flatten_dict(v)
            else:   
                if k in dict_res.keys():
                    dict_res[k] = dict_res[k]+v  
                else:  
                    dict_res[k] = v
    
    flatten_dict(d)
    return dict_res

# flatten a nested dictionary keeping parent key reference
def flat_dict_in(d):
    dict_res = {}
      
    def flatten_dict_in(d,pre = ''):
        for k, v in d.items():    
            if type(v)==dict:
                flatten_dict_in(v,k)
            else:   
                if pre+'_'+k in dict_res.keys():
                    dict_res[pre+'_'+k] = dict_res[pre+'_'+k]+v  
                else:  
                    dict_res[pre+'_'+k] = v
    
    flatten_dict_in(d)
    return dict_res

d = {'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}

print(flat_dict_in(d))

# count of possibility of combination of numbers with power N to sum to target

def combo_sum(Target, N):
    
    arr = [i**N for i in range(1,int(Target**(1/2)+1))]
      
    def combo_sum_rec(Target,arr,partial=[]):
        cnt = 0
        total = sum(partial)
        if Target == total :
            cnt += 1
            print(partial,Target, cnt)
            
        if total >= Target:
            return cnt

        for i in range(len(arr)):
            arr_left = arr[i+1:]
            cnt += combo_sum_rec(Target,arr_left,partial + [arr[i]])
        
        return cnt
        
    
    x = combo_sum_rec(Target,arr)
    return x


print(combo_sum(100, 3))
