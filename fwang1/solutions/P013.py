class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        print s
        dict = {"I": 1, "V": 5, "X": 10, "L" : 50, "C":100, "D":500, "M":1000}
        res = 0
        for c in s:
            res += dict[c]

        return res
if __name__ == "__main__":
	input = "MDCCC"
	print Solution().romanToInt(input)
