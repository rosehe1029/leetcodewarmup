'''
Author: philosophylato
Date: 2022-10-27 11:10:29
LastEditors: philosophylato
LastEditTime: 2022-10-27 11:32:26
Description: your project 
version: 1.0
'''

from multiprocessing import dummy


def removeNthFromEnd(head:ListNode,n:int):
    dummy=ListNode(0,head)
    p1,p2=dummy,dummy
    for i in range(n):
        p1=p1.next
    
    while p1.next is not None:
        p1=p1.next
        p2=p2.next
    
    p2.next=p2.next.next
    return dummy.next
    