class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     反转元素
    #     时间复杂度：O(n)
    #     空间复杂度：O(n)
    #     """
    #     n = len(nums)
    #     k = k % n
    #     nums[:] = nums[n - k:] + nums[:n - k]

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        三次反转：
        反转第一段，[4,3,2,1,5,6,7]
        反转第二段，[4,3,2,1,7,6,5]
        反转整体，[5,6,7,1,2,3,4]
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        k = k % n
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)

if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7], 3))