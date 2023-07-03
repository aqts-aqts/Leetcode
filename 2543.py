class Solution(object):
    dp = {}
    def isReachable(self, targetX, targetY):
        def solve(x, y):
            if x == 1 and y == 1:
                return True
            if x < 0 or y < 0:
                return False
            if isinstance(x, float) or isinstance(y, float):
                return False
            
            self.dp[(x, y)] = solve(x, y - x) if x > 0 and (x, y - x) not in self.dp else self.dp[(x, y - x)] if x > 0 else False
            self.dp[(x, y)] = self.dp[(x, y)] or solve(x - y, y) if y > 0 and (x - y, x) not in self.dp else self.dp[(x - y, y)] if y > 0 else False
            self.dp[(x, y)] = self.dp[(x, y)] or solve(x / 2, y) if x > 0 and (x / 2, y) not in self.dp else self.dp[(x / 2, y)] if x > 0 else False
            self.dp[(x, y)] = self.dp[(x, y)] or solve(x, y / 2) if y > 0 and (x, y / 2) not in self.dp else self.dp[(x, y / 2)] if y > 0 else False
            return self.dp[(x, y)]
        return solve(targetX, targetY)
    
# code performs differently on leetcode vs local idk why