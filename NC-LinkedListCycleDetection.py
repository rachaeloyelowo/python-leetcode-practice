# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list_dict = {}
        p = head # the pointer starts at the head
        index = 0 # creates an index for the nodes in the linked list

        while p: # runs until the pointer points to the end of the linked list
            if p not in linked_list_dict: # checks if the current node isn't in the dictionary
                linked_list_dict[p] = index # if its not, will add it along with its index 
                index += 1 # increases the index
            else:
                return True # if it is, then there is a loop
            p = p.next # moves the pointer along the linked list
        return False # if the while loop ends, that means there's no cycle