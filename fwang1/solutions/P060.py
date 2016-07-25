import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        res = []
        list = range(1, n + 1)
     	tmp = list[:]
     	while tmp:
     		sub_len = math.factorial(len(tmp) - 1)
     		num = tmp[k / sub_len] 
     		k %= sub_len
     		tmp.remove(num)
     		res.append(str(num))
     	return ''.join(res)

if __name__ == "__main__":
	print Solution().getPermutation(3, 5)

