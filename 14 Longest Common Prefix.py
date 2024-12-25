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
            accumulator_curr = ""
            if i == 0:
                accumulator_curr = strs[i]
            else:
                j = 0
                compare = min(len(accumulator), len(strs[i]))
                while j < compare:
                    if accumulator[j] == strs[i][j]:
                        accumulator_curr += strs[i][j]
                        j += 1
                    else:
                        break
            accumulator = accumulator_curr
            i += 1
        return accumulator