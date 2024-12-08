class Solution(object):
    def halvesAreAlike(self, string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        string = string.lower()
        left = string[:len(string) // 2]
        right = string[len(string) // 2:]
        l = 0
        r = 0
        for c in left:
            if c in vowels: l += 1
        for c in right:
            if c in vowels: r += 1
        return l == r