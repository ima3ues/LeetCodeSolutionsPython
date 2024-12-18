# Easy
# 67 Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# Base Code
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

# Solution
class Solution(object):
    def addBinary(self, a, b):
        length_a = len(a)
        length_b = len(b)
        compare = max(length_a, length_b)


        i = 0
        prev_num = None



        while i < compare:



            if prev_num == None:
                if index_a < 0: 
                    now = b[index_b]
                    prev_num = None

                elif index_b < 0:
                    now = a[index_a] 
                    prev_num = None

                else:
                    num = a[index_a] + b[index_b]
                    if num == 0 or num == 1:
                        now = num
                        prev_num = None
                    elif num == 2:
                        now = 0
                        prev_num = 1
                    elif num == 3:
                        now = 1
                        prev_num = 1
                
                returnl.append(now)


            else:
                if index_a < 0 and index_b < 0:
                    now = prev_num

                elif index_a < 0: 
                    num = b[index_b] + prev_num
                    if num == 0 or num == 1:
                        now = num
                        prev_num = None
                    elif num == 2:
                        now = 0
                        prev_num = 1
                    elif num == 3:
                        now = 1
                        prev_num = 1

                elif index_b < 0:
                    num = a[index_a] + prev_num 
                    prev_num = None
                    if num == 0 or num == 1:
                        now = num
                        prev_num = None
                    elif num == 2:
                        now = 0
                        prev_num = 1
                    elif num == 3:
                        now = 1
                        prev_num = 1

                else:
                    num = a[index_a] + b[index_b] + prev_num
                    if num == 0 or num == 1:
                        now = num
                        prev_num = None
                    elif num == 2:
                        now = 0
                        prev_num = 1
                    elif num == 3:
                        now = 1
                        prev_num = 1

            i += 1