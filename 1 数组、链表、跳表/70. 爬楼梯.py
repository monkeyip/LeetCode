class Solution:
    def climbStairs(self, n):
        # 转换为斐波拉契，循环时间复杂度为O(n)
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))