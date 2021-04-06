class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = defaultdict(lambda: '')
        stack = []

        for num in nums2:
            if stack:
                while stack and stack[-1] < num:
                    mem[stack.pop()] = num
            stack.append(num)

        while stack:
            mem[stack.pop()] = -1

        for i in range(len(nums1)):
            nums1[i] = mem[nums1[i]]

        return nums1
