class Solution:
    # def plusOne(self, digits):
    #     n = len(digits)
    #     s = 0
    #     for i in range(n):
    #         s += digits[i] * (10**(n-1-i))
    #     return [int(x) for x in str(s+1)]

    # def plusOne(self, digits):
    #     n = len(digits)
    #     s = 0
    #     for i in digits:
    #         s = s * 10 + i
    #     return [int(x) for x in str(s+1)]

    def plusOne(self, digits):
        '''
        从最低位开始做加法运算
        '''
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        ans = [0] * (len(digits) + 1)
        ans[0] = 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.merge([4,5,6,0,0,0], 3, [1,2,5], 3))