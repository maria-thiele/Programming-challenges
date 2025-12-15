"""
Solutions of the problem: 2. Add Two Numbers (difficulty: medium)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers which are formatted as a linked list in reverse order
        
        Args:
        --------
            l1 (Optional[ListNode]): non-empty linked list of the first number
            l2 (Optional[ListNode]): non-empty linked list of the second number

        
        Returns:
        --------
            Optional[ListNode]: linked list of the sum of the two numbers l1 and l2; 
                                like the two numbers the linked list is in reverse order
        """
        # print(l1, l1.val, l1.next)

        # compute first sum
        nodes_sum = l1.val + l2.val
        transfer = 0 
        if nodes_sum < 10:
            startNode = ListNode(nodes_sum)
        else:
            transfer = 1
            startNode = ListNode(nodes_sum - 10)

        previous = startNode
        currentl1 = l1.next
        currentl2 = l2.next

        # loop through all other entries of l1 and l2 and compute the sum
        while True:
            
            # loop breaks when no number has more elements left to be summed
            if (currentl1 == None) and (currentl2 == None):
                if transfer != 0:
                    new_node = ListNode(transfer)
                    previous.next = new_node
                break
            
            # check if any of the numbers has no more elements left
            # if that is the case, set the element to 0 (will not affect the addition but allows for normal summation operations)
            if currentl1 == None:
                current1 = 0
                nextl1 = None
            else:
                current1 = currentl1.val
                nextl1 = currentl1.next
            
            if currentl2 == None:
                current2 = 0
                nextl2 = None
            else:
                current2 = currentl2.val
                nextl2 = currentl2.next
            
            # compute the sum considering the transfer value
            current_sum = current1 + current2 + transfer
            
            # apply the transfer 
            if current_sum < 10:
                transfer = 0
                new_node = ListNode(current_sum)
            else:
                transfer = 1
                new_node = ListNode(current_sum - 10)
            
            # connect the computations to form a linked list
            previous.next = new_node
            previous = new_node

            # select the next elements from the linked lists
            currentl1 = nextl1
            currentl2 = nextl2
        
        return startNode