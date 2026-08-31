from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)

        if max(cnt.values()) > (n + 1) // 2:
            return ""

        res = [''] * n
        i = 0

        for char, freq in cnt.most_common():
            for _ in range(freq):
                res[i] = char
                i += 2
                if i >= n:
                    i = 1
        return "".join(res)