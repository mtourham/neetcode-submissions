class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        sorted_list = []
        ret = []
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
        sorted_list = sorted(mp.keys(), key=lambda x: mp[x], reverse=True)
        for r in range(k):
            ret.append(sorted_list[r])
        return ret