# Easy
# 28 Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Base Code
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

# Solution
class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = 0
        return_val = -1
        while i < len(haystack):
            if j < len(needle):
                if haystack[i] == needle[j]:
                    return_val = i
                    j += 1
                else:
                    return_val = -1
                    i = i - j
                    j = 0
                i += 1
            else: 
                break
        if j == len(needle):
            return return_val - (len(needle) - 1)
        else:
            return -1