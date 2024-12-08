class Solution:
    def seperate(self, num, limit):
        elements = (num // limit) + (1 if num % limit else 0)
        min_num = num // elements
        return (min_num, elements - 1)

    def minimumReplacement(self, nums):
        # Observation: The last element never needs to be modified in the optimal solution.
        # Observation 2: Break each element that is larger than the next into the largest possible numbers that are still smaller than the next number to achieve the optimal solution.
        # Iterate from the end of the array to the first, if we see an element that is larger than the previous one, we split it into the largest numbers that are still smaller than the previous number. Repeat until the entire array is sorted.
        n = len(nums)
        prev = nums[n - 1]
        i = n - 2

        total = 0
        
        while i >= 0:
            if nums[i] > prev:
                s = self.seperate(nums[i], prev)
                total += s[1]
                prev = s[0]
            else:
                prev = nums[i]
            i -= 1

        return total