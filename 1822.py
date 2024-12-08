class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1
        for num in nums:
            if num < 0:
                sign = not sign
            elif num == 0:
                return 0
        return 1 if sign else -1