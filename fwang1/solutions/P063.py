class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                elif i == j == 0:
                    res[i][j] = 1
                else:
                    up = res[i - 1][j] if i > 0 else 0
                    left = res[i][j - 1] if j > 0 else 0
                    res[i][j] = up + left
        return res[-1][-1]

if __name__ == "__main__":
    print Solution().uniquePathsWithObstacles([[0]])
