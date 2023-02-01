'''
Author: philosophylato
Date: 2022-10-27 11:34:53
LastEditors: philosophylato
LastEditTime: 2022-10-27 13:45:17
Description: your project
version: 1.0
'''
from tkinter.messagebox import NO


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: #排除空链表的特殊情况，以及设置递归条件
            return head
        else:
            tmp = self.reverseList(head.next)
            tailOftmp = tmp
            while tailOftmp.next is not None: #寻找链表尾部
                tailOftmp = tailOftmp.next
            tailOftmp.next = head #将head设置为链表的尾节点
            head.next = None #将链表尾部置为空以免产生环链表
            return tmp







