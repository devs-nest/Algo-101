# @Author: Araika Singh <NonZeroExitCode>
# @Date:   2021-03-20T00:17:56+05:30
# @Email:  roseymods@gmail.com
# @Last modified by:   NonZeroExitCode
# @Last modified time: 2021-03-20T01:26:20+05:30
# Link to question: https://leetcode.com/problems/contains-duplicate/

class ContainsDuplicate(object):
    def containsDuplicate(self, nums):

        # Keep a set that keeps track of distict elements in nums array
        hashSet = set()

        # Traversing the nums array
        for num in nums:

            # If the set doesn't contain the nums[i] then add it to set
            if num not in hashSet:
                hashSet.add(num)
            else:
                # In case the set already contains the number then return true
                return True

        # In case no element was found again the set, hence no duplicate present
        return False
