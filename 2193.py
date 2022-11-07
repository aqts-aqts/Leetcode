# Minimum Number of Moves to Make Palindrome
class Solution:
    def minMovesToMakePalindrome(self, s):
        string = list(s)
        swaps = 0
        for i in range(len(string) // 2):
            j = len(string) - i - 1
            if string[i] != string[j]:
                lpos = i
                rpos = j
                while string[i] != string[rpos]:
                    rpos -= 1
                while string[j] != string[lpos]:
                    lpos += 1
                if j - rpos < lpos - i:
                    swaps += j - rpos
                    for v in range(rpos, j):
                        string[v] = string[v + 1]
                else:
                    swaps += lpos - i
                    for v in range(lpos, i, -1):
                        string[v] = string[v - 1]
        return swaps