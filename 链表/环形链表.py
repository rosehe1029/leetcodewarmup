'''
Author: philosophylato
Date: 2022-10-27 10:12:44
LastEditors: philosophylato
LastEditTime: 2022-10-27 10:18:32
Description: your project
version: 1.0
'''
def hasCycle(head :ListNode)->bool:
    if head is None:
        return False
    fast=head
    slow=head
    while fast.next is not None and fast.next.next is not None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

    


