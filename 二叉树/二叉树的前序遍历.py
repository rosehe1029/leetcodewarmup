'''
Author: philosophylato
Date: 2022-11-03 11:33:11
LastEditors: philosophylato
LastEditTime: 2022-11-03 14:54:04
Description: your project
version: 1.0
'''
def preorderTraversal(root):
    #递归
    res=list()
    def preordef(root):
        if not root: return 
        res.append(root.val)
        preordef(root.left)
        preordef(root.right)
    preordef(root)
    return res

    #迭代
    if not root: return 
    res=list()
    stack,node=[],root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node=node.left
        node=stack.pop()
        node=node.right
    return res
    