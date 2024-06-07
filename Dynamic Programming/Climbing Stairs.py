from functools import cache


class Solution:
    @cache
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


obj = Solution()
result = obj.climbStairs(4)
print(result)
