'''
Author: philosophylato
Date: 2022-10-01 22:13:34
LastEditors: philosophylato
LastEditTime: 2022-10-01 22:17:17
Description: your project
version: 1.0
'''
def isPalindrome(s):
    n=len(s)
    i=0
    j=n-1
    while i<j:
        if s[i].isalnum() ==False:
            i+=1
            continue
        if s[j].isalnum()==False:
            j-=1
            continue
        if s[i].lower() !=s[j].lower():
            return False
        i+=1
        j-=1
    return True
    