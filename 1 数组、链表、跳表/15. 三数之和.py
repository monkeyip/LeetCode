class Solution:
    # def threeSum(self, nums):
    #     '''
    #     哈希表：将三数之和转换为a+b=-c，对数组进行排序(理由稍后解释), 再对排序后的数组进行遍历,
    #     将每个元素的相反数作为key, 元素所在的位置作为value存入哈希表中,
    #     两次遍历数组不断检查 a + b 之和是否存在于哈希表中
    #     时间复杂度：O(n^2)
    #     空间复杂度：O(n)
    #     '''
    #     if not nums or len(nums) < 3:
    #         return []
    #     '''先对数组排序, 遍历数组遇到与前一个元素相同的情况可直接跳过'''
    #     nums.sort()
    #     target_hash = {-x: i for i, x in enumerate(nums)} # 遇到相同的元素，后者index会覆盖前者index
    #     res = []
    #     res_hash = {}
    #     for i, first in enumerate(nums):
    #         '''当前元素与前一个元素相同时, 可直接跳过以优化性能
    #         （后一个元素能发现的结果一定会包含在前一个元素的结果中）'''
    #         if i > 0 and first == nums[i - 1]:
    #             continue
    #         for j, second in enumerate(nums[i + 1:]):
    #             '''检查两数之和是否存在于哈希表中'''
    #             if first + second in target_hash:
    #                 target_index = target_hash[first + second]
    #                 if target_index == i or target_index == i + j + 1:
    #                     continue
    #                 '''将找到的结果存入另一个哈希表中, 避免包含重复结果'''
    #                 row = sorted([first, second, nums[target_index]])
    #                 key = ",".join([str(x) for x in row])
    #                 if key not in res_hash:
    #                     res.append(row)
    #                     res_hash[key] = True
    #     return res

    def threeSum(self, nums):
        '''
        双指针：先做排序，固定一个数，移动另外左右边界两个数，通过计算三数之和>,<,=的情况分别做处理，
        当然也要剔除重复值
        时间复杂度：O(n^2) 其中固定指针k循环复杂度 O(N)O(N)，双指针 i，j 复杂度 O(N)O(N)
        空间复杂度：O(1) 指针使用常数大小空间
        '''
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums)-2):
            if nums[k] > 0: break # 1. because of j>i>k,so k+i+j>0
            if k >0 and nums[k] == nums[k-1]: continue # 2. skip the same nums[k]
            i, j = k+1, len(nums)-1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))