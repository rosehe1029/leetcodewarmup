'''
Author: philosophylato
Date: 2022-10-27 15:11:01
LastEditors: philosophylato
LastEditTime: 2022-10-27 15:15:28
Description: your project
version: 1.0
'''
def flatten(self,head:'Node'):
    def flat(cur):
        if not cur:return 
        if not cur.child:
            if not cur.next:return cur
            else :  return flat(cur.next)
        tmp=cur.next
        cur.next=cur.child
        cur.child=None
        cur.next.prev=cur
        child_end=flat(cur.next)
        child_end.next=tmp
        if tmp:
            tmp.prev=child_end
            return flat(tmp)
        return child_end
    flat(head)
    return head
    












