class Solution(object):
    def uniquePathsIII(self, grid):
        n = len(grid)
        m = len(grid[0])
        squares = sum(row.count(0) for row in grid) + 1
        start = None

        for i, row in enumerate(grid):
            for j, s in enumerate(row):
                if s == 1: 
                    start = (i, j)
                    break

        def solve(row, col, visited = set()):
            if grid[row][col] == -1: return 0
            elif grid[row][col] == 2: return len(visited) == squares

            visited.add((row, col))

            up = solve(row - 1, col, visited.copy()) if (row - 1, col) not in visited and row > 0 else 0
            down = solve(row + 1, col, visited.copy()) if (row + 1, col) not in visited and row + 1 < n else 0
            right = solve(row, col + 1, visited.copy()) if (row, col + 1) not in visited and col + 1 < m else 0
            left = solve(row, col - 1, visited.copy()) if (row, col - 1) not in visited and col > 0 else 0
            
            return up + down + right + left
        
        return solve(start[0], start[1])