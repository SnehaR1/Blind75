# print the list of two indices,the values at which will sum to the provided target value


class Solution:
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.extend([i, j])
                    break
        return ans


list1 = [1, 2, 3, 4, 5]
target = 3
obj = Solution()
answer = obj.twoSum(list1, target)
print(answer)
