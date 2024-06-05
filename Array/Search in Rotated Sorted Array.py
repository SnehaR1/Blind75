class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


obj = Solution()
nums = [5, 6, 7, 8, 4, 3, 2, 1]
res = obj.search(nums, 8)
print(res)
