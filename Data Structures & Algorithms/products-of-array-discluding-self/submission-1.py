class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            res[i] = pre
            pre *= num
        pre = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= pre
            pre *= nums[i]
        
        return res