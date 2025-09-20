# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(lo, hi, arr):
            if hi < lo :
                return
            
            mid = lo + (hi - lo) // 2

            root = TreeNode()
            root.val = arr[mid]
            root.left = build_tree(lo, mid - 1, arr)
            root.right = build_tree(mid + 1, hi, arr)

            return root

        return build_tree(0, len(nums) -1 , nums)