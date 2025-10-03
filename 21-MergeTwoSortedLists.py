# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        m = ListNode()
        ptr_m = m

        while ptr1 != None and ptr2 != None :
            if ptr1.val > ptr2.val : 
                ptr_m.next = ptr2
                ptr2 = ptr2.next
            else :
                ptr_m.next = ptr1
                ptr1 = ptr1.next
            ptr_m = ptr_m.next

        if ptr1 == None and ptr2 != None :
            ptr_m.next = ptr2
    
        if ptr2 == None and ptr1 != None : 
            ptr_m.next = ptr1

        return m.next