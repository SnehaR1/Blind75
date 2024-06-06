class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > 0 else a


obj = Solution()
result = obj.getSum(1, 3)
print(result)
