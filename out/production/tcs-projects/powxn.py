class Solution:
    def myPow(self, x: float, n: int) -> float:
        for i in range(n):
            x *= x
        if n < 0:
            return 1 / x
        else:
            return x
    
s = Solution()
print(s.myPow(2.0, 10))