# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArraytoBST(self,nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArraytoBST(nums[:mid])
        root.right = self.sortedArraytoBST(nums[mid+1:])
        return root
    def inorderTraversal(self,root):
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_nodes = self.inorderTraversal(root)
        return self.sortedArraytoBST(sorted_nodes)
