class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # Let dp[i][j] be the maximal rectangle at the node (i, j), without going further down or right. Express as a pair (r, c), where r is the number of rows, and c is the number of columns of the rectangle.
        # Observation 1: When there are multiple ways to get the maximal rectangle, we have to consider all of them.
        # Observation 2: Not always is the maximum rectangle able to be formed by the maximal rectangle of adjacent nodes.
        # Observation 3: We have to consider ALL rectangles, regardless of their size.
        # Observation 4: We do not have to consider rectangles which are overlapped in a bigger rectangle. Example: (1, 6) and (1, 7). We do not have to consider (1, 6).
        # Observation 5: There is a maximum of 3 rectangles that we have to consider for every node, one which goes straight up, one which goes straight left, and one which is formed by the left-most and top-most corner of rectangle given by the adjacent nodes.

        matrix = list(list(map(int, row)) for row in matrix)
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[set([]) for _ in range(cols + 1)] for _ in range(rows + 1)]
        rectangle = 0

        for i in range(1, cols + 1):
            dp[0][i].add((0, 0))

        for i in range(1, rows + 1):
            if matrix[i - 1][0]:
                (pair,) = dp[i - 1][1]
                y = pair[1] + 1
                dp[i][1].add((1, y))
                rectangle = max(rectangle, y)
            else:
                dp[i][1].add((0, 0))

            for j in range(2, cols + 1):
                if not matrix[i - 1][j - 1]:
                    dp[i][j].add((0, 0))
                    continue

                if matrix[i - 2][j - 1] and matrix[i - 1][j - 2]:
                    last_x = 0
                    last_y = 0

                    min_x = 0
                    min_y = 0

                    for top_pair in dp[i - 1][j]:
                        for left_pair in dp[i][j - 1]:
                            topleft = j - top_pair[0] + 1
                            toptop = i - top_pair[1]
                            leftleft = j - left_pair[0]
                            lefttop = i - left_pair[1] + 1

                            left = max(topleft, leftleft)
                            top = max(toptop, lefttop)

                            x = j - left + 1
                            y = i - top + 1

                            if x > last_x or y > last_y:
                                dp[i][j].add((x, y))
                                rectangle = max(rectangle, x * y)

                                last_x = x
                                last_y = y
                                
                                overlaps = []
                                for pair in dp[i][j]:
                                    if pair == (x, y):
                                        continue
                                    if pair[0] <= x and pair[1] <= y:
                                        overlaps.append(pair)
                                for pair in overlaps:
                                    dp[i][j].remove(pair)

                                min_x = max(x, min_x)
                                min_y = max(y, min_y)

                    max_x = max(pair[0] for pair in dp[i][j - 1]) + 1
                    max_y = max(pair[1] for pair in dp[i - 1][j]) + 1
                    
                    if max_x > min_x:
                        dp[i][j].add((max_x, 1))
                    if max_y > min_y:
                        dp[i][j].add((1, max_y))
                    rectangle = max(rectangle, max(max_x, max_y))

                elif matrix[i - 2][j - 1] and not matrix[i - 1][j - 2]:
                    y = max(pair[1] for pair in dp[i - 1][j]) + 1
                    rectangle = max(rectangle, y)
                    dp[i][j].add((1, y))

                elif not matrix[i - 2][j - 1] and matrix[i - 1][j - 2]:
                    x = max(pair[0] for pair in dp[i][j - 1]) + 1
                    rectangle = max(rectangle, x)
                    dp[i][j].add((x, 1))

                else:
                    rectangle = max(rectangle, 1)
                    dp[i][j].add((1, 1))

        return rectangle