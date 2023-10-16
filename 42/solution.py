from typing import List


def is_left_peak( current, next ):
    return current > next

def is_right_peak( current, next ):
    return current < next

def get_volume( start_ind, end_ind ):
    return end_ind-start_ind-1


class Solution:
    def trap(self, height: List[int]) -> int:

        for i in range(len(height)-1):
            
            # only check from the leftmost peak
            if is_left_peak( height[i], height[i+1] ):
                return self.chunk( height[i:] )

        return 0
    
    def chunk( self, height, volume=0):

        if len(height) == 0:
            return volume

        h0 = height[0]
        if (h0 - height[1]) > 1:
            height[0] -= 1
            return self.chunk( height, volume=volume )

        return self.chunk( height[1:] )



answer = Solution().trap( [2,0,1,2,0,2] )
print ()
print (answer)
#print (Solution().trap( [0,1,0,2,1,0,1,3,2,1,2,1] ))

