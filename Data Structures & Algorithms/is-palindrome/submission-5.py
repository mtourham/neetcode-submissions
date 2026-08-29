class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        while i < len(res):
            for j in range(len(res) - 1, -1, -1):
                if i == j:
                    return True
                elif res[i] != res[j]:
                    return False
                else:
                    i += 1
        return True