class Solution:
    def canJump(self, nums):
        i = 0
        for j in nums:
            if i < 0:
                return False
            elif j > i:
                i = j
            i -= 1
        return True


obj = Solution()
result = obj.canJump([2, 3, 1, 1, 4])
print(result)
