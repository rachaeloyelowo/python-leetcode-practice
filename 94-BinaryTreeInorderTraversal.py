# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorderTraversal_Helper(headNode, nodeList) : 
            if headNode == None :
                return
            inorderTraversal_Helper(headNode.left, nodeList)
            nodeList.append(headNode.val)
            inorderTraversal_Helper(headNode.right, nodeList)


        inorderNodes = []
        inorderTraversal_Helper(root, inorderNodes)
        return inorderNodes