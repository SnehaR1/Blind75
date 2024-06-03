class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currentSum = nums[0]
        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        return maxSum


obj = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = obj.maxSubArray(nums)
print(result)
