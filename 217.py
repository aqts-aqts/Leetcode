# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums):
        visited = dict()
        for n in nums:
            if n in visited: return True
            visited[n] = 1
        return False