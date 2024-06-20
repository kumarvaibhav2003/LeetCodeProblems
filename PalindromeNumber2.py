'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''


class Solution(object):
    def isPalindrome(self, num):
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also, if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0. Only 0 satisfy this property.
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        reverted_number = 0
        while num > reverted_number:
            reverted_number = reverted_number * 10 + num % 10
            num //= 10
            # print('reverted number',reverted_number,'num:',num)
            # When the length is an odd number, we can get rid of the middle of the digit by revertedNumber / 10 For
            # example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
            # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get
            # rid of it.
        return num == reverted_number or num == reverted_number // 10

obj = Solution()
number = 1221
print(obj.isPalindrome(number))