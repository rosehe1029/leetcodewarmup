'''
Author: philosophylato
Date: 2022-10-27 14:48:14
LastEditors: philosophylato
LastEditTime: 2022-10-27 14:58:46
Description: your project
version: 1.0
'''
from cgi import parse_header


class ListNode:
    def __init___(self,val=0,next=None):
        self.val=val
        self.next=next

def addTwoNumbers(l1:Optional[ListNode],l2:Optional[ListNode]):
    phead=ListNode(0)
    cur=phead
    carry=0
    while l1 and l2:
        ref=l1.val+l2.val +carry
        carry=ref // 10
        node=ListNode(ref %10)
        cur.next=node
        cur=node
        l1=l1.next
        l2=l2.next
    while l1:
        ref=l1.val +carry
        carry =ref // 10
        node=ListNode(ref%10 )
        cur.next=node
        cur=node
        l2=l2.next
    if carry >0:
        node=ListNode(carry)
        cur.next=node
        cur=node
    return phead.next
    