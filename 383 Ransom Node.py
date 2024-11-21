# Easy
# 383 Ransom Node
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Base Code
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

# Solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_list = list(magazine)

        for each_char in ransomNote:
            if each_char in magazine_list:
                # remove the character from magazine (avoid repeat usage)
                magazine_list.remove(each_char)
            else:
                return False
        # if all characters are found, return True
        return True