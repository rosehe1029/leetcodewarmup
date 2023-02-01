'''
You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/root-equals-sum-of-children
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
Example 1:

Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

Example 2:

Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.

Constraints:

    The tree consists only of the root, its left child, and its right child.
    -100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/root-equals-sum-of-children
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#Definition for a binary tree node
from optparse import Option


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def checkTree(self,root:Option[TreeNode])->bool:
        return True if root.val == (root.left.val+root.right.val) else False

