# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # ensure we have at least the root
        if not nums:
            return None

        # we will be creating a stack where each element is the following tuple:
        # (left index of nums, right index of nums, parent node, child side),
        # where the left and right indices set the bounds of the values in
        # nums the current node considers, and child side refers to which side
        # of the parent node that the current node will be set to (more clear below)

        # create the root, which is the "first parent"
        l, r = 0, len(nums) - 1  # initial left and right bounds of nums
        i = (l + r) // 2         # center of the bounds of nums we view
        root = TreeNode(nums[i])

        # create a stack of the first two children values; split bounds of
        # parent's left and right bounds in half using the center position,
        # then remember the side of the parent (root) to set that child to
        stack = [(l, i-1, root, 'l'),
                 (i+1, r, root, 'r')]

        # while there are more children to create
        while stack:
            # extract the information for a child
            l, r, parent, side = stack.pop()

            # only create the child if it looks at a valid left and right bound
            # in nums, so the left index <= right index; this ensures we stop
            # adding children after we've exhausted the valid positions in nums
            if l <= r:
                i = (l + r) // 2  # center position of bounds

                # create the child node from the center position,
                # and set the corresponding child side in the parent
                child = TreeNode(nums[i])
                if side == 'l':
                    parent.left = child
                else:
                    parent.right = child

                # add the information for the two children of the current child,
                # splitting the left and right bounds of the current child in half
                # using the center position, then remember the side of the child
                # (which becomes the parent for its children) to set next children
                stack.append((l, i - 1, child, 'l'))
                stack.append((i + 1, r, child, 'r'))

        return root
