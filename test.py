l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 100

  
# output list
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
       
            
                
