def rev_lis(l,i=0):
    if  i != len(l)-1:
        rev_lis(l,i+1)
    print (l[i])

rev_lis('pramanik')


def sum_nested(lis):
    total = 0

    for i in range(len(lis)):
          if type(lis[i])== list:
              total = sum_nested(lis[i])
          else:
              total += lis[i]
    
    return total

print (sum_nested([[4,5],[7,8,[20]],100]))

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

def print_recur(lis, i=0):
    print (lis[i])
    if i != len(lis)-1:
        print_recur(lis,i+1)

print_recur('pramanik')



