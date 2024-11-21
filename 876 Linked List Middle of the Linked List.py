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
        list_length = 1
        second_list = []
        while head.next:
            list_length += 1
            second_list.append(head.val)
            head = head.next
        new_start_index = (list_length // 2) + 1
        mid_list = second_list[new_start_index:]
        return mid_list


