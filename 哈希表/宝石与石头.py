'''
Author: philosophylato
Date: 2022-11-02 15:03:38
LastEditors: philosophylato
LastEditTime: 2022-11-02 15:06:38
Description: your project
version: 1.0
'''
def numJewlsInstones(jewels,stones):
    count=0
    hash_set=set()
    for jewel in jewels:
        hash_set.add(jewel)
    for stone in stones:
        if stone in hash_set:
            count+=1
    return count
    