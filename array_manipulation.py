#https://www.hackerrank.com/challenges/crush/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import functools as ft

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0 for i in range(n)]
    l = len(queries)
    for i in range(l):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        for j in range(b-a+1):
            arr[a-1+j] = arr[a-1+j]+k
    c = ft.reduce(lambda x,y:max(x,y),arr)
    return c
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
