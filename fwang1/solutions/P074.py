class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix: return False
        else: return self.binary_search(matrix, target)
        
    def binary_search(self, matrix, target):
        m,n = len(matrix), len(matrix[0])
        if target < matrix[0][0] and target > matrix[-1][-1]: return False
    	start, end = 0, m * n - 1
        while start < end:
    	    mid = (start + end) / 2
            i,j = mid / n, mid % n
            print (start, mid, end,i,j)
    	    if target < matrix[i][j]: end = mid - 1
    	    elif target > matrix[i][j]: start = mid + 1
    	    else: return True
        return False

