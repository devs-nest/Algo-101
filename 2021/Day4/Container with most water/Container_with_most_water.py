class Solution:

    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer approach
        1. one pointer start from the start
        2. one pointer start from the end
        3. calculate the areas
        4. update max area.
        5. return max area once 1st pointer = 2nd pointer
        """
        firstp = 0
        secondp = len(height)-1
        maxarea = 0

        while firstp != secondp:
            currfirst = height[firstp]
            secondfirst = height[secondp]
            hlength = secondp - firstp
            area = hlength*min(currfirst, secondfirst)
            if maxarea < area:
                maxarea = area

            if currfirst >= secondfirst:
                secondp -= 1
            else:
                firstp += 1

        return maxarea
