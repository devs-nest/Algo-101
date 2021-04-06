class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        x = len(nums3)
        if(x % 2 == 0):
            x = x//2
            a = nums3[x]
            x = x-1
            a = float(a + nums3[x])/2.0
            return a
        else:
            x = x//2
            return (float(nums3[x]))
