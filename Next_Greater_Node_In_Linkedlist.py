# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Initialize an empty stack to store the indices of elements
        stack = []
        # Initialize an empty list to store the result
        result = []
        
        # Convert the linked list to a list
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        # Iterate through the list to find the next greater node
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            stack.append(i)
            result.append(0)
        
        return result
