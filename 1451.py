class Solution:
    def arrangeWords(self, text):
        words = text.split()
        words[0] = words[0].lower()
        words = sorted(words, key = lambda word: len(word))
        words[0] = words[0].capitalize()
        return ' '.join(words)