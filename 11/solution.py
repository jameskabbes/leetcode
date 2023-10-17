from typing import List

def get_area( index1, index2, height1, height2 ):
    return abs( index2-index1 ) * min(height1, height2)

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        for i in range(len(height)-1):
            for j in range( 1, len(height) ):
                area = get_area( i, j, height[i], height[j] )
                max_area = max( area, max_area )        

        return max_area

print (Solution().maxArea([1,8,6,2,5,4,8,3,7]))