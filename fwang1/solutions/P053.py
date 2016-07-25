class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        sum = nums[0]
        for i in range(len(nums) - 1):
            nums[i + 1] = max(nums[i] + nums[i + 1], nums[i + 1])
            sum = max(nums[i + 1], sum)
        return sum

if __name__ == "__main__":
	print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])