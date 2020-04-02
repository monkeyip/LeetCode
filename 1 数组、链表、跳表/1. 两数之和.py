class Solution:
    def twoSum(self, nums, target):
        '''
        利用哈希表记录另外一个元素的值
        时间复杂度：O(n)
        '''
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))