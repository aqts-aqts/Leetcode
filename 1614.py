class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = max_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1  # Increase depth for every '('
                max_depth = max(max_depth, current_depth)  # Update max depth if current depth is greater
            elif char == ')':
                current_depth -= 1  # Decrease depth for every ')'
        return max_depth