class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length: 
                continue
            finished = True
            for i in range(length, n):
                if s[i] != s[i % length]:
                    finished = False
                    break
            if finished:
                return True
        return False