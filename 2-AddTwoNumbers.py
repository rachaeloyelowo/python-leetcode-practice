# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_1 = l1
        ptr_2 = l2

        carry_over = 0
        answer = ListNode()

        answer_ptr = answer

        while ptr_1 and ptr_2 :
            answer_ptr.next = ListNode((((ptr_1.val) + (ptr_2.val) + carry_over) % 10))
            carry_over = ((ptr_1.val) + (ptr_2.val) + carry_over) // 10

            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
            answer_ptr = answer_ptr.next
        
        if ptr_1 :
            while ptr_1 :
                answer_ptr.next = ListNode((ptr_1.val + carry_over) % 10)

                carry_over = ((ptr_1.val) + carry_over) // 10                
                ptr_1 = ptr_1.next
                answer_ptr = answer_ptr.next
        
        if ptr_2 : 
            while ptr_2 :
                answer_ptr.next = ListNode((ptr_2.val + carry_over) % 10)
                
                carry_over = ((ptr_2.val) + carry_over) // 10
                ptr_2 = ptr_2.next
                answer_ptr = answer_ptr.next

        if carry_over != 0 :
            answer_ptr.next = ListNode(carry_over)

        return answer.next