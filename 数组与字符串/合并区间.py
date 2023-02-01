'''
Author: philosophylato
Date: 2022-10-03 15:46:04
LastEditors: philosophylato
LastEditTime: 2022-10-03 15:53:24
Description: your project
version: 1.0
'''
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merges=list()
    for interval in intervals:
        if not merges or merges[-1][-1] <interval[0]:
            merges.append(interval)
        else:
            merge[-1][-1]=max(merges[-1][-1],interval[1])
    return merges



    
