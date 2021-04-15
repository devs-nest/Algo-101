# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.best = 1

        def depth(root):
            if not root:
                return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best - 1
