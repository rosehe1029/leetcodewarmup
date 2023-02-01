'''
Author: philosophylato
Date: 2022-11-20 22:16:42
LastEditors: philosophylato
LastEditTime: 2022-11-20 22:23:42
Description: your project
version: 1.0
'''
def inorderTraversal(self,root):
    '''
    :type root:TreeNode
    :rtype:List[int]
    '''
    stack=[]
    res=[]
    node=root
    while stack or node:
        while node:
            stack.append(node)
            node=node.left
        node=stack.pop()
        res.append(node.val)










def