'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def middleNode(self,head:ListNode)->ListNode:
        if head is None:
            return None
        
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow

def create_linked_list(nums):
    if len(nums)==0:
        return None
    head=ListNode(nums[0])
    cur=head
    for i  in range(1,len(nums)):
        cur.next=ListNode(nums[i])
        cur=cur.next
    return head

def print_linked_list(list_node):
    if list_node is None:
        return 
    cur=list_node
    while cur:
        print(cur.val,'->',end='')
        cur=cur.next
    print('null')

if __name__=='__main__':
    nums=[1,2,3,4,5,6,7,8]
    head=create_linked_list(nums)
    solution=Solution()
    result=solution.middleNode(head)
    print('结果')
    print_linked_list(result)


