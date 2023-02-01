'''
Author: philosophylato
Date: 2022-10-27 14:04:43
LastEditors: philosophylato
LastEditTime: 2022-10-27 14:14:10
Description: your project
version: 1.0
'''
def oddEvenList(head:ListNode)->ListNode:
    if not head or not head.next or not head.next.next: return head
    odd,even,head1=head,head.next,head.next
    while even and even.next:
        odd.next,even.next=odd.next.next,even.next.next
        odd,even=odd.next,even.next
    odd.next=head1
    return head
    

