from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        1. Loop through nums and store the number of occurences in a dictionary of each unique number
        2. Only keep unique values of nums: list(set(nums))
        3. Using the new list, create a new dictionary where the key is the number and the value its index
        4. Using an O(n^2) nested for loop, find the missing puzzle piece called complement that would fit, look for it in the values_at_inds dict
        5. Consider all numbers which had 2 or more occurences
        """

        print (nums)

        # { number: count of number in list }
        nums_counts = {}
        for i in range(len(nums)):
            if nums[i] not in nums_counts:
                nums_counts[ nums[i] ] = 1
            else:
                nums_counts[ nums[i] ] += 1

        # keep only one copy of each number
        nums = list(set(nums))
        print (nums)

        # { number: index of number in list }
        values_at_inds = {}
        for i in range(len(nums)):
            values_at_inds[ nums[i] ] = i

        # Three Sum
        solutions = []
        for i in range( len(nums)-2 ):
            for j in range( i+1, len(nums) -1 ):

                complement = -(nums[i] + nums[j])
                print (nums[i], nums[j], complement, end ='')

                if complement in values_at_inds:
                    k = values_at_inds[complement]

                    # we don't want to use a value that j has already taken throughout the for loop
                    if ( k > j ):
                        print (' - yes')
                        solutions.append( [ nums[i], nums[j], nums[ k ] ] )

                else:
                    print()

        # check for doubles and triples
        for i in range( len(nums) ):

            # there is a double, we can use more than one of them
            if nums_counts[ nums[i] ] >= 2:
                complement = -(nums[i] + nums[i])
                if complement in values_at_inds:
                    k = values_at_inds[complement]
                    if (i != k):
                        solutions.append( [ nums[i], nums[i], nums[ k ] ] )

            # there is a triple occurrence
            if nums_counts[ nums[i] ] >= 3 and nums[i] == 0:
                solutions.append( [ nums[i], nums[i], nums[ i ] ] )

        return solutions

    

#print (Solution().threeSum( [ -1, 0, 1, 2, -1, -4 ] ) )
#print (Solution().threeSum( [ 0, 1, 1 ] ) )
#print (Solution().threeSum( [ 0, 0, 0 ] ) )
print (Solution().threeSum( [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6] ) )

#[-4,2,2],[-2,-2,4]