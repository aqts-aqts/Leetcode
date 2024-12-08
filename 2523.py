class Solution(object):
    def closestPrimes(self, left, right):
        global prev, mindist, minpair
        mindist = 1e8
        minpair = []
        prev = -1e9
        def eratosthenes(l, r):
            global prev, mindist, minpair
            prime = [1 for i in range(r + 1)]
            p = 2
            while (p ** 2 <= r):
                if prime[p]:
                    for i in range(p * p, r + 1, p): prime[i] = False
                p += 1

            for p in range(2, r + 1):
                if prime[p] and p >= l:
                    if p - prev < mindist:
                        mindist = p - prev
                        minpair = [prev, p]
                    prev = p
        eratosthenes(left, right)
        if not minpair: return [-1,-1]
        return minpair