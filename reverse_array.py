#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    l = len(a)
    if l%2==0:
        for i in range(int(l/2)):
            a1 = a[i]
            b1 = a[l-1-i]
            a[i] = b1
            a[l-1-i] = a1
            print (a)
    else :
        for i in range(int((l-1)/2)):
            a1 = a[i]
            b1 = a[l-1-i]
            a[i] = b1
            a[l-1-i] = a1
        
    return (a)       
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
