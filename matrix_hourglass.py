#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    siz = len(arr[0])
    hg_num = siz-2 ** 2
    hg_sum = [[0 for i in range(siz-2)] for j in range(siz-2)]
    s=0
    for y in range(siz-2):
        for x in range (siz-2):
           s= arr[y][x]+arr[y][x+1]+arr[y][x+2]+arr[y+1][x+1]+arr[y+2][x]+arr[y+2][x+1]+arr[y+2][x+2]
           hg_sum[y][x] = s
     
    mx = max(max(x) for x in hg_sum)
        
    return mx
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
