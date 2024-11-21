# Easy
# 876 Middle of the Linked List (Linked List)
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Base Code
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

# Solution
class Solution(object):
    def middleNode(self, head):
        # traverse the linked list to collect all **nodes**
        nodes = []  # store nodes, not values
        current = head
        
        while current:
            nodes.append(current) 
            current = current.next
        
        # calculate the middle index
        middle_index = len(nodes) // 2  
        
        # return the middle **node**
        # why? - the problem explicitly asks to return the middle **node** of the linked list
        return nodes[middle_index]