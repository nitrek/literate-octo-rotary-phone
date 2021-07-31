#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countConnections function below.
def isSafe(i,j,row,col,matrix):
  
    if 0 <= i < row and 0<=j < col:
        print(matrix[i][j],i,j)
        return True
    return False 
    
def countConnections(matrix):
    row = len(matrix)
    col = len(matrix[0])
    con = 0 
    
    
    for i in range(row):
        for j in range(col):
            print("--")
            print(matrix[i][j],i,j)
            if (matrix[i][j] == 1):
                if isSafe(i+1,j,row,col,matrix) and ( matrix[i][j] == matrix[i+1][j]):
                    con = con + 1
                if isSafe(i,j+1,row,col,matrix) and ( matrix[i][j] == matrix[i][j+1]):
                    con = con + 1
                if isSafe(i+1,j+1,row,col,matrix) and ( matrix[i][j] == matrix[i+1][j+1]):
                    con = con + 1
                if isSafe(i-1,j,row,col,matrix) and ( matrix[i][j] == matrix[i-1][j]):
                    con = con + 1
                if isSafe(i-1,j+1,row,col,matrix) and ( matrix[i][j] == matrix[i-1][j+1]):
                    con = con + 1
                if isSafe(i-1,j-1,row,col,matrix) and ( matrix[i][j] == matrix[i-1][j-1]):
                    con = con + 1
                if isSafe(i,j-1,row,col,matrix) and ( matrix[i][j] == matrix[i][j-1]):
                    con = con + 1
                if isSafe(i-1,j-1,row,col,matrix) and ( matrix[i][j] == matrix[i-1][j-1]):
                    con = con + 1
                    
    return int(con/2)

def countConnections2(matrix):
    row = len(matrix)
    col = len(matrix[0])
    print(row,col)
    con = 0
    for i in range(row):
        for j in range(col):
            #print(i,j)  
            if (i+1< row ) and matrix[i+1][j] == matrix[i][j]:
                #print(matrix[i][j])
                print("a("+str(i)+","+str(j)+")->("+str(i+1)+","+str(j)+")")
                con = con +1
            if (i+1< row ) and (j+1< col ) and matrix[i+1][j+1] == matrix[i][j]:
                #print(matrix[i+1][j+1])
                print("b("+str(i)+","+str(j)+")->("+str(i+1)+","+str(j+1)+")")
                con = con +1
            if (j+1< col ) and matrix[i][j+1] == matrix[i][j]:
                #print(matrix[i][j+1])
                print("c("+str(i)+","+str(j)+")->("+str(i)+","+str(j+1)+")")
                con = con +1
            if (i-1 >= 0 ) and matrix[i-1][j] == matrix[i][j]:
                #print(matrix[i-1][j])
                print("d("+str(i)+","+str(j)+")->("+str(i-1)+","+str(j)+")")
                con = con +1
            if (i-1 >= 0 ) and (j-1>= 0 ) and matrix[i-1][j-1] == matrix[i][j]:
                #print(matrix[i-1][j-1])
                print("e("+str(i)+","+str(j)+")->("+str(i-1)+","+str(j-1)+")")
                con = con +1
            if (j-1 >= 0 ) and matrix[i][j-1] == matrix[i][j]:
                #print(matrix[i][j-1])
                print("f("+str(i)+","+str(j)+")->("+str(i)+","+str(j-1)+")")
                con = con +1
            if (i+1< row ) and (j-1>=0 ) and matrix[i+1][j-1] == matrix[i][j]:
                #print(matrix[i+1][j-1])
                print("g("+str(i)+","+str(j)+")->("+str(i+1)+","+str(j-1)+")")
                con = con + 1
            if (j+1< col ) and (i-1>=0 ) and matrix[i-1][j+1] == matrix[i][j]:
                #print(matrix[i-1][j+1])
                print("h("+str(i)+","+str(j)+")->("+str(i+1)+","+str(j)+")")
                con = con + 1
    return int(con/2)         
if __name__ == '__main__':