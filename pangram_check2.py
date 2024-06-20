# Program to check if a sentence is Pangram or not.
"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
        for i in range(26):
            curr_char = chr(ord('a') + i)
            # print(curr_char)

            # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
            if sentence.find(curr_char) == -1:
                return False

        # If we manage to find all 26 letters, it is a pangram.
        return True

obj = Solution()
print(obj.checkIfPangram('abc'))