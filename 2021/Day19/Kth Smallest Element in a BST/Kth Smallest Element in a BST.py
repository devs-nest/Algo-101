# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        i = 0
        stack = []
         node = root
          while node or stack:
               while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                i += 1
                if i == k:
                    return node.val
                node = node.right
