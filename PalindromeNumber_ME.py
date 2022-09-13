'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''
# My Logic: First store the individual digits in an array then check if first digit is equal to last digit, then go to second digit and
# second last digit and check the same and use flags to store the results at each stage

class Solution(object):

    def get_length(self,x):
        """
        function to return the length of an integer

        :param x: int
        :return: int
        """
        count = 1
        x = abs(x)
        while (x // 10):
            count += 1
            x = x // 10
        return count

    def isPalindrome(self, x):
        """
        function to check whether the given number is palindrome
        :type x: int
        :rtype: bool
        """
        # check for negative number, always non-palindrome
        if x < 0:
            return False

        # check for single digit and zero, always palindrome
        if self.get_length(x) == 1 or x == 0:
            return True

        x = abs(x)
        digits = []
        while x // 10 or x % 10:
            digit = x % 10
            digits.append(digit)
            x = x // 10
        # print(digits)
        j = len(digits) - 1
        flag = False
        # final flag as True because if any condition would give False then AND will produce False
        final_flag = True
        for i in range(len(digits)//2):
            if digits[i] == digits[j]:
                flag = True
                final_flag = final_flag and flag
            else:
                flag = False
                final_flag = final_flag and flag
            j = j - 1
        if final_flag == True:
            return True
        else:
            return False



obj = Solution()
number = 100021
# print(obj.get_length(number))
print(obj.isPalindrome(number))
