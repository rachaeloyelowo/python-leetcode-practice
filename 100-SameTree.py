# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrderTraversal(p_root , q_root, is_same) : 
            if (p_root == None and q_root == None) : 
                return
            if (p_root == None and q_root != None) : 
                is_same[0] = False
                return
            if (p_root != None and q_root == None) : 
                is_same[0] = False
                return

            if (p_root.val != q_root.val) : 
                is_same[0] = False
                return
            else : 
                preOrderTraversal(p_root.left, q_root.left, is_same)
                preOrderTraversal(p_root.right, q_root.right, is_same)

        is_same = [True]
        preOrderTraversal(p , q, is_same)
        return is_same[0]