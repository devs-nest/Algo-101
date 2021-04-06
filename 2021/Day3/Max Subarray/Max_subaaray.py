class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Track a running sum of consecutive numbers and the global max sum.
        running_sum = nums[0]
        max_sum = running_sum

        for num in nums[1:]:

            # As long as the running sum is positive, adding it to the next
            # number will continue to grow the sum. Once the running sum
            # becomes negative, adding it to the next number will only
            # shrink that number, so we reset the running sum to the next
            # number.

            # The following line could've been rewritten more intuitively as:
            #    if running_sum >= 0:
            #        running_sum += num

            #    elif running_sum < 0:
            #        running_sum = num

            running_sum = max(running_sum + num, num)

            # Update max_sum if current_sum > max_sum.
            max_sum = max(max_sum, running_sum)

        return max_sum
