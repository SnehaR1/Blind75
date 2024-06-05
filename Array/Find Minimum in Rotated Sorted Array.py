class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        res = float("inf")
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res


obj = Solution()
nums = [4, 5, 6, 1, 2, 3]
result = obj.findMin(nums)
print(result)
