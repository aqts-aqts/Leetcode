class Solution(object):
    def numRescueBoats(self, people, limit):
        n = len(people)
        people = sorted(people)
        
        left = 0
        right = n - 1
        
        boats = 0
        while left <= right:
            boats += 1
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
        return boats