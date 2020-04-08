class Solution:
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     while n > 0:
    #         if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
    #             nums1[m + n - 1] = nums2[n - 1]
    #             n -= 1
    #         else:
    #             nums1[m + n - 1] = nums1[m - 1]
    #             m -= 1

    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        sort()方法实现
        """
        nums1[m:m + n] = nums2
        nums1.sort()

if __name__ == "__main__":
    s = Solution()
    print(s.merge([4,5,6,0,0,0], 3, [1,2,5], 3))