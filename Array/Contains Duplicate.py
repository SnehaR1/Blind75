# Method1
class Solution1:
    def containsDuplicate(self, nums):

        return False if len(set(nums)) == len(nums) else True


# Method2
class Solution2:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


obj1 = Solution1()
result1 = obj1.containsDuplicate([1, 1, 2, 3, 4])
print(result1)
obj2 = Solution2()
result2 = obj2.containsDuplicate([1, 2, 3, 4, 5, 6])
print(result2)
