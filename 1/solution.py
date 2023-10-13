from typing import List

class Solution:

    # Time Complexity: O(n) Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [i, d[complement]]
            d[nums[i]] = i

    """    
    # Time Complexity: O(n**2) Space Complexity: 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range( i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """

print (Solution().twoSum( [5,7,10,13], 17 ))