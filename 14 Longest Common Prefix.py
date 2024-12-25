# Easy
# 14 Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Base Code
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

# Solution
class Solution(object):
    # just a reminder, the question asked for prefix
    def longestCommonPrefix(self, strs):
        i = 0
        accumulator = ""
        for each_alpha in strs[0]:
            if strs[0][i] == each_alpha:
                i += 1
                accumulator = accumulator + each_alpha
            else:
                break

        return accumulator