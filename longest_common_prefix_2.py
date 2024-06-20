"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        res = ""
        v = sorted(v)
        # print(v)
        for i in range(min(len(v[0]),len(v[-1]))):
            if v[0][i] != v[-1][i]:
                return res
            res += v[0][i]
        return res

obj = Solution()
strs = ["flower","flow","flought"]
print(obj.longestCommonPrefix(strs))