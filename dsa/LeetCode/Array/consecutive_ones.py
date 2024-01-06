#Question.: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, windowSize = 0, 0
        for n in nums:
            if n == 1:
                windowSize += 1
            else:
                res = max(res, windowSize)
                windowSize = 0
        res = max(res, windowSize)

        return res
        