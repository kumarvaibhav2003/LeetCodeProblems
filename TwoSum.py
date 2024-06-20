'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Example 1:

Input: nums = [2,7,11,15], target = 9   
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
# Logic is to check second number as target - first number
# This is the brute force approach.
# Time Complexity : O(n^2)
# Space Complexity: O(1). The space required does not depend on the size of the input array, so only constant space is used.
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

obj = Solution()
nums = [-1,2,-3,1]
target = 0
print(obj.twoSum(nums, target))