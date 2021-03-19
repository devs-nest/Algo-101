# @Author: Kshitiz Miglani
# SDE @AMAZON | Founder @Devsnest.in
# @Link to question: https://leetcode.com/problems/two-sum/
class TwoSumPython(object):
    def twoSum(self, nums, target):
        # Creating a HashMap to keep track of numbers and their indices
        nummap = {}

        # Traversing through the array
        # Say for testcase array = {0, 1, -1, 2} if required sum is 0.
        # Then the present element should have a number (target - present element)
        # Like for n = 2, the list should have (0 - 2) = -2 to have a sum = 0
        for i in range(len(nums)):
            num = nums[i]

            # if the map contains (target - present element) then we got our pair and
            # hence the required indices is to be returned
            if target - num in nummap:
                return [nummap[target-num], i]

            nummap[num]=i
# If no pair is found, there is no pair then nothing is returned
