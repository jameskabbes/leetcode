from typing import List

def get_area( index1, index2, height ):
    return abs(index2-index1)*( min(height[index1], height[index2]) )


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left_ind = 0
        right_ind = len(height)-1

        max_area = 0
        while left_ind < right_ind:
            max_area = max( max_area, get_area( left_ind, right_ind, height ) )

            if height[left_ind] < height[right_ind]:
                left_ind += 1
            else:
                right_ind -= 1
        
        return max_area
    
print (Solution().maxArea([1,8,6,2,5,4,8,3,7]))