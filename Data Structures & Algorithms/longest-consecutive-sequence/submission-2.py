class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 1
        numsSet = set(nums)
        streak = 0
        
        for i in range(len(nums)):
            if not nums[i] - 1 in numsSet:
                lenght = 1
                while nums[i] + lenght in numsSet:
                    lenght += 1
                streak = max(lenght, streak)
            
        return streak