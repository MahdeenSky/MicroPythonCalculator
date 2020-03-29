"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)): # loops through the indexes of each of the characters in the array
            for j in range(0,len(nums)): # loops through the indexes for each index of the array
                sum = nums[i] + nums[j] # sum is equal to adding the two values in each index
                if((sum == target) and (i != j)): # sum must equal target and the indexes must be different, inorder to return an output
                    return(i,j) # returns the indexes of the two numbers that equal the target

result = twoSum([2,3,8,10], 18) # test data
print(result)