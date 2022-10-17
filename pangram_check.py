# Program to check if a sentence is Pangram or not.
"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        template = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        chars = [char for char in sentence]
        # print(chars)
        flag = True
        for char in template:
            if char in chars:
                flag = flag and True
            else:
                flag = flag and False
        return flag


obj = Solution()
print(obj.checkIfPangram('the'))
