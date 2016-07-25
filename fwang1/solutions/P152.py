class Solution(object):
    def maxProduct(self, nums):
        _min = _max = res= nums[0] 

        for num in nums[1:]:
            if num < 0: 
                _min, _max = _max, _min
            _min = min(_min * num, num)
            _max = max(_max * num, num)       
            res = max(res, _max)

        return res


if __name__ == "__main__":
	# print Solution().maxProduct([-2,3,-4])
    # print Solution().maxProduct([-2,0,-1])
    # print Solution().maxProduct([0,1,0,2,0,3,4,0,0,0,1,2,3,4,5])
    # print Solution().maxProduct([2,0,3,-2])
        print Solution().maxProduct([11,33,0,-2,3,4,5])

# print Solution().split_list_by_zero([-2,3,-4])

