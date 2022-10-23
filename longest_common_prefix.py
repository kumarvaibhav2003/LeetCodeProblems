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
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = []
    num = len(strs)
    for x in zip(*strs):
        # print(set(x))
        if len(set(x)) == 1:
            # print(x[0])
            prefix.append(x[0])
        else:
            break
    return "".join(prefix)
    # return prefix

strs = ["flower","flow","floght"]
print(longestCommonPrefix(strs))