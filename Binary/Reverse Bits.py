class Solution:
    def reverseBits(self, n):
        val = 0
        for i in range(32):
            res = (n >> i) & 1
            val = val | res << (31 - i)

        return val


obj = Solution()

result = obj.reverseBits(2)
print(result)
