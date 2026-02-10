#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getOptimalClassification' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scores
#  2. STRING labels
#

def getOptimalClassification(scores, labels):
    correct = 0
    greater = []
    less = []
    largest_less = 0
    smallest_greater = 0
    
    for i in range(len(scores)):
        if labels[i] == '1':
            greater.append(scores[i])
        else:
            less.append(scores[i])
            
    largest_less = max(less)
    smallest_greater = min(greater)
    
    if largest_less >= smallest_greater:
        for i in range(smallest_greater-5, largest_less+5):
            temp = 0
            temp_str = ''
            for j in range(0, len(scores)):
                if scores[j] >= i:
                    temp_str += '1'
                else:
                    temp_str += '0'
                    
            for k in range(len(labels)):
                if temp_str[k] == labels[k]:
                    temp += 1
                    
            if temp > correct:
                correct = temp
    else:
        for i in range(largest_less-5, smallest_greater+5):
            temp = 0
            temp_str = ''
            for j in range(0, len(scores)):
                if scores[j] >= i:
                    temp_str += '1'
                else:
                    temp_str += '0'
                    
            for k in range(len(labels)):
                if temp_str[k] == labels[k]:
                    temp += 1
                    
            if temp > correct:
                correct = temp

    return correct
    
    
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input().strip())

    scores = []

    for _ in range(scores_count):
        scores_item = int(input().strip())
        scores.append(scores_item)

    labels = input()

    result = getOptimalClassification(scores, labels)

    fptr.write(str(result) + '\n')

    fptr.close()
