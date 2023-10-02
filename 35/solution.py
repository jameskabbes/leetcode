from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range( len(nums) ):
            if nums[i] >= target:
                return i
        return i+1

print (Solution().searchInsert( [1,3,5,6], 5 ))
print (Solution().searchInsert( [1,3,5,6], 2 ))
print (Solution().searchInsert( [1,3,5,6], 4 ))
