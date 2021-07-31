#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the countSpecialElements function below.
import sys
def countSpecialElements(matrix):
    
    setMaxMin = set()
    print(matrix)
    for i in range(len(matrix)):
        rowmin = sys.maxsize
        rowmax = -sys.maxsize -1
        for j in range(len(matrix[i])):
            if(rowmin == matrix[i][j] or rowmax == matrix[i][j]):
                return -1
            rowmin = min(rowmin,matrix[i][j])
            rowmax = max(rowmin,matrix[i][j])
        setMaxMin.add(rowmin)
        setMaxMin.add(rowmax)
    for j in range(len(matrix[0])):
        colmax = - sys.maxsize -1
        colmin = sys.maxsize
        for i in range(len(matrix)):
            if(colmin == matrix[i][j] or colmax == matrix[i][j]):
                return -1
            colmax = max(colmax,matrix[i][j])
            colmin = min(colmin,matrix[i][j])
            
        # if (colmax in setMaxMin):
        setMaxMin.add(colmax)
        setMaxMin.add(colmin)
    print(setMaxMin)
    return len(setMaxMin) if len(setMaxMin)> 0 else 0

if __name__ == '__main__':