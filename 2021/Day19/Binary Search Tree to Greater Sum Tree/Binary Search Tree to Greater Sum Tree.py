# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def recur(node, sumTillNow):
            if not node:
                return sumTillNow
            node.val += recur(node.right, sumTillNow)
            return recur(node.left, node.val)

        recur(root, 0)
        return root
