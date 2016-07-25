class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum_dict = {}
        list = filter(lambda x: x <= target, candidates)
        list.sort()
        print list
        k = 1
        for i in range(len(candidates)):
        	for j in range(i, i + k):
                
        	   pass# print i, j	


if __name__ == "__main__":
	candidates = [10, 1, 2, 7, 6, 1, 5] 
	target = 8
	Solution().combinationSum2(candidates, target)

