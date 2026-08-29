class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        streak = 0
        
        for i in range(len(nums)):
            lenght = 0
            if not nums[i] - 1 in numsSet:
                lenght = 1
                while nums[i] + lenght in numsSet:
                    lenght += 1

            streak = max(streak, lenght)
            
        return streak