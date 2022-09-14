'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1] # str(x)[::-1] will print the string in reverse order


obj = Solution()
number = 100021
# print(obj.get_length(number))
print(obj.isPalindrome(number))
