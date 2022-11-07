# Plus One
class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        pointer = 0
        while pointer < len(digits) and digits[pointer] == 9:
            digits[pointer] = 0
            pointer += 1
        if pointer == len(digits): digits.append(1)
        else: digits[pointer] += 1
        return digits[::-1]