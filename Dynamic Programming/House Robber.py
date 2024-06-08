class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]
        eve = nums[0]
        odd = nums[1]
        for i in range(2, len(nums)):
            if i % 2 == 0:
                odd = max(eve, odd)
                eve += nums[i]
            else:
                eve = max(eve, odd)
                odd += nums[i]
        return max(eve, odd)


obj = Solution()
result = obj.rob([1, 3, 2, 4, 5])
print(result)
