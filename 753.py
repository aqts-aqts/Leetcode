class Solution:
    def __init__(self):
        self.password = None
        self.visited = set()

    def DFS(self, permutation: str, n: int, k: int) -> bool:
        if len(self.visited) == k ** n:
            return True

        for i in range(k):
            new_permutation = permutation[1:] + str(i)

            if new_permutation not in self.visited:
                self.visited.add(new_permutation)
                self.password += str(i)

                if self.DFS(new_permutation, n, k):
                    return True
                
                self.visited.remove(new_permutation)
                self.password = self.password[:-1]
        return False

    def crackSafe(self, n: int, k: int) -> str:
        # Find Eulerian Path using DFS
        self.password = '0' * n
        self.visited.add(self.password)

        self.DFS(self.password, n, k)  
        return self.password