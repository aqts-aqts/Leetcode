class Solution:
    def sumOfDistancesInTree(self, n, edges):
        # Create an adjacency list for the tree
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # Arrays to store the count of nodes in the subtree and the sum of distances
        count = [1] * n  # Initialize count of each subtree to include the node itself
        answer = [0] * n

        # DFS to calculate count and answer for the root
        def dfs(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        # DFS to adjust answer for all nodes using the answer of their parent
        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + n - count[child]
                    dfs2(child, node)

        # Start the DFS from the root node
        dfs(0, -1)
        dfs2(0, -1)
        return answer