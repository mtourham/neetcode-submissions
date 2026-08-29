class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(res) - 1
        while left < right:
            print("left --> ", res[left], "right --> ", res[right])
            if res[left].lower() != res[right].lower():
                return False
            left += 1
            right -=1 
        return True