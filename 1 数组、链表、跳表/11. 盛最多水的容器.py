class Solution:
    def maxArea(self, height):
        # 双指针法：由左右边界向中间靠拢，只移动值较小的指针
        i, j = 0, len(height)-1
        maxarea = min(height[0],height[-1]) * (len(height)-1)
        while i < j:
            area = min(height[i],height[j]) * (j-i)
            maxarea = max(maxarea,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))