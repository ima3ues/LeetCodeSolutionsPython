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
        while i < len(strs):
            j = 0
            while j < len(accumulator):
                if accumulator[j] == strs[i][j]:
                    j += 1
                    accumulator_curr = accumulator_curr + strs[i-1][j]
                else:
                    break
            accumulator = accumulator_curr
            i += 1