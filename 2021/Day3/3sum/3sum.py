class Solution:#By CyFun
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums, tripluts = list(counter.keys()), set()
        if counter[0] >= 3:
            tripluts.add((0, 0, 0))
        plus, minus = [n for n in nums if n > 0], [
            n for n in nums if n < 0]
        for a in minus:
            for b in plus:
                c = -(a + b)
                if c in counter and ((c != a and c != b) or counter[c] > 1):
                    tripluts.add(tuple(sorted([a, b, c])))
        return tripluts
