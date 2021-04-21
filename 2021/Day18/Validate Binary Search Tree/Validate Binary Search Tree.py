# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.valid(root, -sys.maxsize, sys.maxsize)

    def valid(self, root, l, r):
        if not root:
            return True
        if not (l < root.val < r):
            return False
        return self.valid(root.left, l, root.val) and self.valid(root.right, root.val, r)

    def isValidBST3(self, root):
        pre, stack = None, []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if pre and pre.val >= node.val:
                return False
            pre = node
            root = node.right

    def isValidBST2(self, root):
        ret, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            ret.append(node.val)
            root = node.right
        for i in range(len(ret)-1):
            if ret[i] >= ret[i+1]:
                return False
        return True

    def isValidBST1(self, root):
        ret = []
        self.dfs(root, ret)
        for i in range(len(ret)-1):
            if ret[i] >= ret[i+1]:
                return False
        return True

    def dfs(self, root, ret):
        if root:
            self.dfs(root.left, ret)
            ret.append(root.val)
            self.dfs(root.right, ret)
