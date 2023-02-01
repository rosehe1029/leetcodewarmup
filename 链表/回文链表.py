'''
Author: philosophylato
Date: 2022-10-27 14:24:10
LastEditors: philosophylato
LastEditTime: 2022-10-27 14:38:38
Description: your project
version: 1.0
'''
def isPalindrome(head:ListNode):
    '''
    思路:1.找到链表的中间节点——快慢节点
    2.将后半部分链表反转
    3.比较链表值
    4.还原链表
    '''
    if not head:
        return True
    #1.找到链表前半部分的尾节点
    first_half_end=first_half_of_end(head)
    #2.对链表后半部分进行反转
    second_half=reverse_list(first_half_end.next)
    #3.判断是否为回文链表
    result=True
    first_pos=head
    second_pos=second_half
    while result and second_pos is not None:
        if first_pos.val !=second_pos.val:
            return False
        first_pos=first_pos.next
        second_pos=second_pos.next
    #4.恢复原链表
    reverse_list(second_half)
    return result
    
def first_half_of_end(head):
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next
    return slow

def reverse_list(head):
    prev=None
    curr=head
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

    
