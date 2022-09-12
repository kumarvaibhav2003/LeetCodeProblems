'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# My logic: start from zero index and check addition with index 1, 2,3 ... If sum is equal to target then break.
# Else Exhaust till the end. Then start with 1 index and check addion with index 2, 3, 4 ... If sum is equal to target then exit.
# num[i] >= 0 for checking positive numbers
# num[i] < 0 for checking negative numbers
# Why exit not break: break will break the current loop only, so inner loop with break but not the outer loop, so exit

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range (i, len(nums)):
                # print('i:',i,'j:',j)
                if nums[i] >= 0: #and nums[i]<=target:
                    sum = nums[i]+nums[j]
                    if sum == target and i!=j:
                        return i, j
                        exit()
                if nums[i] < 0: #and nums[i] > target:
                    sum = nums[i]+nums[j]
                    if sum == target and i!=j:
                        return i, j
                        exit()

obj = Solution()
nums = [2,7,11,15]
target = 9
print(obj.twoSum(nums, target))
