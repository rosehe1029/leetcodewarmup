'''
Author: philosophylato
Date: 2022-09-11 16:26:22
LastEditors: philosophylato
LastEditTime: 2022-09-11 17:22:25
Description: your project
version: 1.0
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from syslog import LOG_WARNING
import heapq,random

def findKthLargest(nums,k):
    heap=[]
    for num in nums:
        heapq.headpush(heap,num)
    if len(heap)>k:
        heapq.heappop(heap)
    return heap[0]

def findKthLargest(nums,k):
    def findTopKth(low,high):
        pivot=random.randint(low,high)
        nums[low],nums[pivot]=nums[pivot],nums[low]
        base=nums[low]
        i=low 
        j=low+1
        while j<=high:
            if nums[j]>base:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
            j+=1
        nums[low],nums[i]=nums[i],nums[low]
        if i==k-1:
            return nums[i]
        elif i>k-1:
            return findKthLargest(low,i-1)
        else :
            return findKthLargest(i+1,high)
        return findKthLargest(0,len(nums)-1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(arr: List[int], low: int, high: int) -> int:
            pivot = arr[low]                                        # 选取最左边为pivot

            left, right = low, high     # 双指针
            while left < right:
                
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处
                
                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处
            
            arr[left] = pivot           # pivot放置到中间left=right处
            return left
        
        def randomPartition(arr: List[int], low: int, high: int) -> int:
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            return partition(arr, low, high)                        # 调用partition函数

        def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
            # mid = partition(arr, low, high)                   # 以mid为分割点【非随机选择pivot】
            mid = randomPartition(arr, low, high)               # 以mid为分割点【随机选择pivot】
            if mid == k-1:                                      # 第k小元素的下标为k-1
                return arr[mid]                                 #【找到即返回】
            elif mid < k-1:
                return topKSplit(arr, mid+1, high, k)           # 递归对mid右侧元素进行排序
            else:
                return topKSplit(arr, low, mid-1, k)            # 递归对mid左侧元素进行排序
        
        n = len(nums)
        return topKSplit(nums, 0, n-1, n-k+1)                   # 第k大元素即为第n-k+1小元素

