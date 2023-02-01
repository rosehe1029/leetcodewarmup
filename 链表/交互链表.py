'''
Author: philosophylato
Date: 2022-10-27 10:39:26
LastEditors: philosophylato
LastEditTime: 2022-10-27 11:06:55
Description: your project
version: 1.0
'''
from tkinter.tix import ListNoteBook


def getIntersectionNode(headA:ListNode,headB:ListNode)->ListNode:
    '''
    思路：两个指针分别从两个链表的开始遍历到结尾，然后再分别从另一个
    链表开始遍历，当两个指针相等时，便是相交
    方法：双指针
    '''
    if not headA or not headB:
        return None
    p1=headA
    p2=headB
    while p1 !=p2:
        p1=headB if p1 is None else p1.next
        p2=headA if p2 is None else p2.next
    return p1
    


