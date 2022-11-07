# Maximum Building Height
class Solution:
    def maxBuilding(self, n, restrictions):
        restrictions.sort()
        if not restrictions or restrictions[0][0] != 1:
            restrictions = [[1, 0]] + restrictions
        elif restrictions[0][0] == 1:
            restrictions[0][1] = 0  

        for i in range(len(restrictions) - 1):
            restrictions[i + 1][1] = min(restrictions[i + 1][1], restrictions[i][1] + restrictions[i + 1][0] - restrictions[i][0])
        highest = n - restrictions[-1][0] + restrictions[-1][1]
        for i in range(len(restrictions) - 1, 0, -1):
            restrictions[i - 1][1] = min(restrictions[i - 1][1], restrictions[i][1] + restrictions[i][0] - restrictions[i - 1][0])
            highest = max(highest, (restrictions[i][0] - restrictions[i - 1][0] + restrictions[i - 1][1] + restrictions[i][1]) // 2)
        return highest