'''
Author: philosophylato
Date: 2022-10-27 10:22:37
LastEditors: philosophylato
LastEditTime: 2022-10-27 10:27:45
Description: your project
version: 1.0
'''
def detectCycle(head:ListNode):
    if not head:
        return None
    dict={}
    while head:
        if head in dict:
            return dict[head]
        dict[head]=head
        head=head.next
    return None
    
