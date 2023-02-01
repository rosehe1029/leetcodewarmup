'''
Author: philosophylato
Date: 2022-10-01 21:52:03
LastEditors: philosophylato
LastEditTime: 2022-10-01 22:05:19
Description: your project
version: 1.0
'''
def merge(nums1,m,nums2,n):
    if (n<1):
        return 
    if (m<1):
        nums1[0:n]=nums2[0:n]
        return 
    k=m+n-1
    i=m-1
    j=n-1
    while k>=0:
        if (nums1[i]>nums2[j] and i>=0) or (j<0 and i>=0):
            nums1[k]=nums1[i]
            k-=1
            i-=1
        if (nums2[j] >= nums1[i] and j>=0) or (i <0 and j>=0):
            nums1[k]=nums2[j]
            k-=1
            j-=1
            
