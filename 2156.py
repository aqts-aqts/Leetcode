class Solution(object):
    def get_alpha_val(self, c):
        return ord(c) - ord('a') + 1
    
    def subStrHash(self, s, power, modulo, k, hashValue):
        if modulo == 1:
            return s[:k] # Anything modulo 1 is just 0, so either all substrings are valid or none of them are in this case, and since the problem always generates an answer we can just return the first k characters
        n = len(s)
        
        # Refer to https://en.wikipedia.org/wiki/Modular_arithmetic
        # ≡ is the congruence operator

        power_mods = [1] # Precompute modulo powers
        for _ in range(1, k):
            power_mods.append((power_mods[-1] * power) % modulo) # ab mod m = (b(a mod m)) mod m
        
        total = 0
        for i in range(n - k, n):
            total += (power_mods[i - n + k] * self.get_alpha_val(s[i])) % modulo # (a + b) mod m ≡ (a mod m) + (b mod m)
        lptr = n - k
        rptr = n - 1

        matches = [] # Stack to find earliest occurence (first substring)
        if total % modulo == hashValue:
            matches.append((lptr, rptr))
        
        while lptr > 0:
            total -= (power_mods[k - 1] * self.get_alpha_val(s[rptr])) % modulo # (a - b) mod m ≡ (a mod m) - (b mod m)

            lptr -= 1

            total = (total * power) % modulo # ab mod m ≡ b(a mod m) mod m
            total += self.get_alpha_val(s[lptr])
            total %= modulo
 
            rptr -= 1

            if total == hashValue: # Push match to stack
                matches.append((lptr, rptr))
                
        if matches:
            l, r = matches.pop() # Get latest match (which will be the first substring)
            return s[l:r + 1]
        else:
            pass