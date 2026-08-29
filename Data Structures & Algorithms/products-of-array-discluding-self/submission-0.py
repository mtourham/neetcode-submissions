class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        ret = []
        
        for i in range(len(nums)):
            ret.append(pre)
            pre *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            ret[j] *= post
            post *= nums[j]

        return ret
