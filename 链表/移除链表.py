'''
Author: philosophylato
Date: 2022-10-27 13:47:53
LastEditors: philosophylato
LastEditTime: 2022-10-27 13:54:08
Description: your project
version: 1.0
'''
def removeElements(self,head:ListNode,val:int)->ListNode:
    while head and head.val == val: head=head.next
    if not head:return head
    pre=head
    cur=head.next
    while cur:
        if cur.val == val:
            cur=cur.next
            pre.next=cur
        else:
            pre=pre.next
            cur=cur.next
        return head
        
