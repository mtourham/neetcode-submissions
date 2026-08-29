class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = set()
        for num in nums:
            if num not in mp:
                mp[num] = 0
            mp[num] += 1
        return sorted(mp.keys(), key = lambda x : mp[x], reverse = True)[0:k]