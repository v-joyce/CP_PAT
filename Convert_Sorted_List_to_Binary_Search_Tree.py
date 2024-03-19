# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        def find_middle(start,end):
            slow = start
            fast = start
            while fast!=end and fast.next!=end:
                slow = slow.next
                fast = fast.next.next
            return slow
        def convert_to_bst(start,end):
            if start==end:
                return None
            middle = find_middle(start,end)
            root = TreeNode(middle.val)
            root.left = convert_to_bst(start,middle)
            root.right = convert_to_bst(middle.next,end)
            return root
        return convert_to_bst(head,None)
