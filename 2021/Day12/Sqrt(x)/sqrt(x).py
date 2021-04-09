class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1
