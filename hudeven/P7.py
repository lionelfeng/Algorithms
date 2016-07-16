class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483648
        MIN_INT = -2147483647
        res = 0;
        p = x if x >= 0 else -x
        while p != 0:
            digit = p % 10
            if res < MAX_INT / 10 or ( res == MAX_INT / 10 and digit <= MAX_INT % 10):
                res = res * 10 + digit
            else:
                return 0
            p = p / 10
        return res if x >= 0 else -res
