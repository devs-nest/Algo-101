# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#generate queue and append root to queue
#while there are nodes in the queue,
#iterate through the number of nodes in the queue
#(this is the number of nodes in the next level)
#pop queue(0), add queue(0).val to current ans list and append queue(0)'s children to queue
#append ans to final_list and reset ans = []
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list
