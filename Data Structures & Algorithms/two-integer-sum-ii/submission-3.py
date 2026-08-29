class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(numbers)

        for i in range(n):
            complement = target - numbers[i]
            if complement in numMap:
                return [min(numMap[complement], i) + 1, max(numMap[complement], i) + 1]
            numMap[numbers[i]] = i

        return []