'''
Author: philosophylato
Date: 2022-10-27 09:32:58
LastEditors: philosophylato
LastEditTime: 2022-10-27 10:07:42
Description: your project
version: 1.0
'''
import gc
from lib2to3.pytree import Node
from os import TMP_MAX
class MyLinkedList(object):
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.head=None
    def get(self,index):
        if (index<0 or self.head=None):
            return -1
        else:
            count=0
            cur=self.head
            while (count<index and cur.next !=None):
                count=count+1
                cur=cur.next
            if (count == index):
                return cur.val
            else:
                return -1
    def addAtHead(self,val):
        node=Node(val)
        node.next=self.head
        self.head=node
    def addAtTail(self,val):
        node=Node(val)
        if (self.head ==None):
            self.head=node
        else :
            cur=self.head
            while (cur.next!=None):
                cur=cur.next
            cur.next=node
    def addAtIndex(self,index,val):
        if (index <=0):
            self.addAtHead(val=val)
        elif (self.head!=None):
            count=0
            cur=self.head
            while (count<index-1 and cur.next!=None):
                count=count+1
                cur=cur.next
            if (count==index-1):
                node=Node(val)
                node.next=cur.next
                cur.next=node
    
    def deleteAtIndex(self,index):
        if (self.head!=None):
            if (index ==0):
                temp=self.head
                self.head=temp.next
                del tmp   
                gc.collect()
            elif (index >0 ):
                count =0
                cur=self.head
                while (count <index -1 and cur.next !=None):
                    count=count+1
                    cur=cur.next
                if (count==index-1):
                    temp=cur.next
                    if (temp!=None):
                        cur.next=temp.next

                    del temp
                    gc.collect()

class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        

