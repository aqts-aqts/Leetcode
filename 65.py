class Solution(object):
    def isNumber(self, s):
        if 'inf' in s or '-inf' in s or 'Inf' in s or '-Inf' in s:
            return False
        try: float(s)
        except ValueError: return False
        else: return True