class Solution:
    def hammingWeight(self, n):
        # binary_val=bin(n)
        # c=binary_val.count("1")
        # return c
        # method 2
        # res=0
        # for i in range(32):
        #     if (n>>i) & 1:
        #         res+=1
        # return res
        # method 3
        # c=0
        # while n:
        #     c+=n&1
        #     n>>=1
        # return c
        # method 4
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res


obj = Solution()
result = obj.hammingWeight(5)
print(result)
