class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        res = [[0] * n] * m

        for i in range(m):
        	for j in range(n):
        		if i == j == 0:
        			res[i][j] = 1
        		else:
	        		up = res[i - 1][j] if i > 0 else 0
	        		left = res[i][j - 1] if j > 0 else 0
	        		res[i][j] = up + left
        
        return res[-1][-1]
        			
if __name__ == "__main__":
	print Solution().uniquePaths(3, 7)
