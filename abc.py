#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)



def maxStrength(n):
    current_num=0
    val=n
    next_num=0
    arry=[]
    for i in range(n*2):
        
        if len(str(val))==1:
            next_num=factorial(val)
            arry.append(val)
            val=next_num     
        else:
            next_num=0
            for i in range(len(str(val))):
                next_num+=factorial(int(str(val)[i]))
                # print(next_num)
            arry.append(val)
            val=next_num
                
    return max(arry)*len(arry)
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = maxStrength(n)

    fptr.write(str(result) + '\n')

    fptr.close()
