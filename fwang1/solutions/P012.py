class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {1: "I", 5:"V", 10: "X", 50:"L", 100: "C", 500: "D", 1000:"M"}

        k = 1
        res = ""
        while num:
        	d = num % 10
        	num /= 10
        	roman = ""
        	if 0 < d < 4:
        		roman = dict[k] * d
        	elif d == 4:
        		roman = dict[k] + dict[5 * k]
        	elif 9 > d > 4:
        		roman = dict[5 * k] + dict[k] * (d - 5)
        	elif d == 9:
        		roman = dict[k] + dict[10 * k]	
        	else:
        		roman = ""
        	k *= 10
        	res = roman + res

        return res

if __name__ == "__main__":
	print Solution().intToRoman(890)