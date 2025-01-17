# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode() # creates empty linked list
        tail = temp_head # assigns the tail to point at on val in list

        while list1 and list2: # continues to go through both list until at least one is empty
            if list1.val > list2.val: # if the val of list 2 is smaller than list 1's
                tail.next = list2 # the tail of the 'new' list will have that val as the next
                list2 = list2.next # list 2's pointer will point to the next val in list 2
            else: 
                tail.next = list1 # the tail of the 'new' list will have that val as the next
                list1 = list1.next # list 1's pointer will point to the next val in list 1
            tail = tail.next # moves the tail pointer over to the next val

        if list1: # checks if remaining vals in list 1
            tail.next = list1 # if so, the tail next val will be the rest of list 1
        elif list2: # check if remaining vals in list 2
            tail.next = list2 # if so, the tail next val will be the rest of list 2

        return temp_head.next # returns the val of the actual head