# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Store node values in a list
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # Initialize maximum twin sum
        max_twin_sum = float('-inf')
        
        # Step 2: Iterate through the first half of the list
        for i in range(len(values) // 2):
            # Calculate twin sum
            twin_sum = values[i] + values[-1 - i]
            # Update maximum twin sum if necessary
            max_twin_sum = max(max_twin_sum, twin_sum)
        
        # Step 4: Return the maximum twin sum
        return max_twin_sum

        
        # Traverse the linked list
        while head:
            # Calculate the complement of the current node's value needed to form a pair sum of k
            complement = n - head.val
            # If the complement is in the set, increment pair_sum
            if complement in seen:
                pair_sum += 1
            # Add the current node's value to the set
            seen.add(head.val)
            # Move to the next node
            head = head.next
        
        return pair_sum
