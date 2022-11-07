# Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums):
        i=0
        for num in nums:
            if len(str(num)) % 2==0: i += 1
        return i