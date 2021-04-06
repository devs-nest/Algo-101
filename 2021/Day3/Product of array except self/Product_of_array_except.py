class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        prod = 1
        num0 = 0
        idx_0 = -1

        for cnt, nm in enumerate(nums):
            if(nm is 0):
                num0 += 1
                idx_0 = cnt
            elif(num0 > 1):
                break
            else:
		#Store partial products into result array
                result[cnt] = prod
                prod *= nm

        if(num0 > 1):
		#This allocate a new array instead one might want
		#to loop over result instead
            return [0]*len(nums)
        elif(num0 == 1):
		#This allocate a new array to save space one might want
		#to loop over result instead
            result = [0]*len(nums)
            result[idx_0] = prod
        else:
            prod = 1
	#Loop into reverse order and multiply partial product
	#by products computed from end
            for cnt in range(len(nums)-1, -1, -1):
                result[cnt] *= prod
                prod *= nums[cnt]

        return result
