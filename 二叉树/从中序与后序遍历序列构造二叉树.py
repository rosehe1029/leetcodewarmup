'''
Author: philosophylato
Date: 2022-11-21 09:57:30
LastEditors: philosophylato
LastEditTime: 2022-11-21 11:05:05
Description: your projectbuil
version: 1.0
'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


# Python版本递归，使用下标，不修改原始传入数据
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def buildTreeHelper(i_l, i_r, p_l, p_r):
            if i_l > i_r or p_l > p_r: return 
            root = TreeNode(postorder[p_r])
            root_idx = hashTable[postorder[p_r]]
            root.left = buildTreeHelper(i_l, root_idx - 1, p_l, p_l + root_idx - 1 - i_l)
            root.right = buildTreeHelper(root_idx + 1, i_r, p_l + root_idx - i_l, p_r - 1)
            return root
        hashTable = {value:i for i, value in enumerate(inorder)}
        return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def buildTree(self,inorder ,postorder):
        if inorder:
            item=postorder.pop()
            node=TreeNode(val=item)
            idx=inorder.index(item)
            node.right=self.buildTree(inorder[idx+1:],postorder)
            node.left=self.buildTree(inorder[:idx],postorder)
            return node
        else :
            return None
            









