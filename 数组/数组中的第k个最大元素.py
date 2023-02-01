'''
Author: philosophylato
Date: 2022-10-01 21:44:20
LastEditors: philosophylato
LastEditTime: 2022-10-01 21:50:55
Description: your project
version: 1.0
'''
def findKthLargest(nums,k):
    n=len(nums)
    if (k>n):
        return 
    index=quickSort(nums,0,n-1,k)
    return nums[k]

def quickSort(nums,l,r,k):
    if l>=r:
        return 1
    p=partition(nums,l,r)
    if p+1 ==k:
        return p
    if p+1 > k:
        return quickSort(nums,l,p-1,k)
    else :
        return quickSort(nums,p+1,r,k)

    def partition(nums,l,r):
        v=nums[l]
        j=l
        i=l+1
        while i<=r:
            if nums[i] >=v:
                nums[j+1],nums[i]=nums[i],nums[j+1]
                j+=1
            i+=1
        nums[l],nums[j]=nums[j],nums[l]