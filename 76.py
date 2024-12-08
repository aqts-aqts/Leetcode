from collections import defaultdict
import sys

class Solution:
    def isValid(self, letter_map: defaultdict[str, int], answer_map: defaultdict[str, int]):
        for ans in answer_map:
            if letter_map[ans] < answer_map[ans]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n:
            return ''

        left = 0
        right = m - 1

        letter_map = defaultdict(int)
        answer_map = defaultdict(int)

        for i in range(m):
            letter_map[s[i]] += 1
            answer_map[t[i]] += 1
        
        min_length = sys.maxsize
        min_window = None

        while True:
            valid = self.isValid(letter_map, answer_map)

            if valid:
                if right - left < min_length:
                    min_length = right - left
                    min_window = s[left:right + 1]

                letter_map[s[left]] -= 1
                left += 1
            elif right < n - 1:
                right += 1
                letter_map[s[right]] += 1
            else:
                break

        return min_window if min_window else ''