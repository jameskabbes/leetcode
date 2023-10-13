from typing import List

class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:

        ### First loop: Sort the list so that [-12, -2, -4, 4, 3, 2, 1] ends up being [1,2,3,4, -12,-2,-4]

        index = 0
        n = len(nums)

        # go through the number at each index and put it in its proper location: 1 belong at index 0, 2 belongs at index 1, etc.
        while index < n:
            
            number = nums[index]
            proper_index = number-1
            
            # three conditions
            # 1. the number is positive
            # 2. the number is not greater than n (if our list is 15 integers long, we shouldn't waste our time organizing the number 20)
            # 3. the proper_index doesn't already contain said number
                    
            if number > 0 and number <= n and nums[ proper_index ] != number:
                nums[index], nums[proper_index] = nums[proper_index], nums[index]
            else:
                index += 1

        
        ### Second loop: returns the first thing out of the ordinary: [1,2,3,4,  6,7,8 ] -> return 5
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        # if nothing in the list is out of the ordinary
        return nums[-1] + 1

print ( Solution().firstMissingPositive( [-3, 1, 4, 0] ) )
