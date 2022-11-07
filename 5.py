# Longest Palindromic Substring
def findLongestPalindromicSubstring(string): # O(n)!
    temp = ''
    for i in string:
        temp += '|' + i
    string = temp + '|'
    substrings = [0] * len(string)
    index = 0
    longest = 0
    for i in range(len(string)):
        s = 2 * index - i
        if longest > i: substrings[i] = min(longest - i, substrings[s])
        else: substrings[i] = 0
        
        try:
            while string[i + 1 + substrings[i]] == string[i - 1 - substrings[i]]: substrings[i] += 1
        except:
            if i + substrings[i] > longest:
                index = i
                longest = i + substrings[i]
    longest = max(substrings)
    index = substrings.index(longest)
    return string[index - longest: index - longest + longest * 2].replace('|', '')

class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]: return s
        return findLongestPalindromicSubstring(s)