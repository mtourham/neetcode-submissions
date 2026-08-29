class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen[nums[r]] = r
        return False