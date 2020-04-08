class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针法：将0和非0元素交换位置
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))