'''
Author: philosophylato
Date: 2022-12-04 20:50:20
LastEditors: philosophylato
LastEditTime: 2022-12-04 20:54:25
Description: your project
version: 1.0
'''
def guessNumber(n):
    left=1
    right=n
    while left <=right:
        res=left+(right-left)//2
        if guess(res)==0:
            return res
        elif guess(res)==1:
            left=res+1
        elif guess(res)==-1:
            