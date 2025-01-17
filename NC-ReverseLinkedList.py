# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = None # the first pointer points at null
        p2 = head # the second pointer points at the head

        while (p2): # goes through the linked list until p2 points to null at the end
            temp = p2.next # temporarily stores where p2 will go to next
            p2.next = p1 # changes where p2 will go to next to the position before
            p1 = p2 # moves p1 over to be p2
            p2 = temp # moves p2 over to where it was meant to go
        return p1 # p2 points at null while p1 points at val before, so we return p1