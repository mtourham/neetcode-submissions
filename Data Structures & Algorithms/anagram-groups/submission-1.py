class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        pos = 0
        res = []

        def ascii_sum(s):
            return sum(ord(char) for char in s)
        
        def is_anagram(s, s1):
            return sorted(s) == sorted(s1)

        for i in range(len(strs)):
            total = ascii_sum(strs[i])
            if total in mp and is_anagram(strs[i], mp[total][0]):
                pos = mp[total][1]
                res[pos].append(strs[i])
            else:
                pos = len(res)
                res.append([strs[i]])
                mp[total] = (strs[i], pos)
                  
        return res