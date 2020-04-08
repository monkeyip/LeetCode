class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     '''
    #     list的pop时间复杂度为O(n),则整体时间复杂度为O(n^2)
    #     '''
    #     pre = 1
    #     while pre < len(nums):
    #         if nums[pre] == nums[pre-1]:
    #             nums.pop(pre)
    #         else:
    #             pre += 1
    #     return pre

    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        只有赋值操作,则整体时间复杂度为O(n),效率更高
        '''
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates())