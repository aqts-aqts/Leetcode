class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            l = ord(s[left])
            r = ord(s[right])
            if not(l > 47 and l < 58) and not(l > 64 and l < 91) and not(l > 96 and l <  123):
                left += 1
                continue
            elif not(r > 47 and r < 58) and not(r > 64 and r < 91) and not(r > 96 and r <  123):
                right -= 1
                continue
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True