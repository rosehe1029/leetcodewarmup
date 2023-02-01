'''
Author: philosophylato
Date: 2022-09-11 16:19:20
LastEditors: philosophylato
LastEditTime: 2022-09-11 16:24:53
Description: your project
version: 1.0
'''
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) :
    if not  list1: return list2 
    if not  list2:return  list1
    if list1.val<list2.val:
        list1.next=mergeTwoLists(list1.next,list2)
        return list1
    else :
        list2.next=mergeTwoLists(list1,list2.next)
        return list2
ListNode()
list1=[1,2,7,9,10]
list2=[3,4,8,12]
print(mergeTwoLists(list1,list2))