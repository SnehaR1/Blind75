class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            min_h = min(height[left], height[right])

            area = min_h * (right - left)
            if area > max_area:
                max_area = area
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution()
result = obj.maxArea(height)
print(result)
