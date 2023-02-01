'''
Author: philosophylato
Date: 2022-10-13 17:12:38
LastEditors: philosophylato
LastEditTime: 2022-10-13 17:17:58
Description: your project
version: 1.0
'''
def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=[0]*len(matrix)
    column=[0]*len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row[i]=1
                column[j]=1
        for i in range(m):
            for j in range(n):
                if row[i]==1 or column[j]==1:
                    matrix[i][j]=0


                    