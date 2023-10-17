from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        max_left = [0,] * n
        max_right = [0,] * n

        # go from left to right, find the maximum height of a bar to the left of the current
        for i in range(1, n):
            max_left[i] = max(height[i-1], max_left[i-1])

        # going from right to left, find the maximum height of a bar to the right of the current
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i+1], max_right[i+1])

        ans = 0
        # going through each bar, add the minimum of the maximum height of bars to the left and right minus the current height
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            if water_level > height[i]:
                ans += water_level - height[i]
        return ans


answer = Solution().trap([4, 1, 2, 3, 4])
print()
print(answer)
# print (Solution().trap( [0,1,0,2,1,0,1,3,2,1,2,1] ))
