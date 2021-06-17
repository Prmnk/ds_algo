arrr = [1,2,3,4,5,6]

def my_prnt(arr):
    def prnt_recr(i):
        if i > len(arr) - 1:
            return
        prnt_recr(i+1)
        print(arr[i])
    prnt_recr(0)