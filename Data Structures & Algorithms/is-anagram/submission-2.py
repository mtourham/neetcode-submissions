class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i, j = 0, 0
        seen = []
        if len(s) != len(t):
            return False
        while i < len(s):
            seen.append(s[i])
            i += 1
        while j < len(t):
            if t[j] in seen:
                seen.remove(t[j])
                j += 1
            else:
                return False
        return True