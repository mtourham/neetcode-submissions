class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        total = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(height[l], maxl)
                total += maxl - height[l]
            else:
                r -= 1
                maxr = max(height[r], maxr)
                total += maxr - height[r]
        return total
