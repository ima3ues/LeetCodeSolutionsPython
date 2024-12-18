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
        leak = None
        index_a = len(a) - 1
        index_b = len(b) - 1
        return_list = []

        while leak != "done":
            
            if leak == None:
                if index_a < 0 and index_b < 0:
                    leak = "done"

                elif index_a < 0: 
                    now = b[index_b]
                    leak = None

                elif index_b < 0:
                    now = a[index_a] 
                    leak = None

                else:
                    num = a[index_a] + b[index_b]
                    if num == 0 or num == 1:
                        now = num
                        leak = None
                    elif num == 2:
                        now = 0
                        leak = 1
                    elif num == 3:
                        now = 1
                        leak = 1
                
            else:
                if index_a < 0 and index_b < 0:
                    now = leak

                elif index_a < 0: 
                    num = b[index_b] + leak
                    if num == 0 or num == 1:
                        now = num
                        leak = None
                    elif num == 2:
                        now = 0
                        leak = 1
                    elif num == 3:
                        now = 1
                        leak = 1

                elif index_b < 0:
                    num = a[index_a] + leak 
                    leak = None
                    if num == 0 or num == 1:
                        now = num
                        leak = None
                    elif num == 2:
                        now = 0
                        leak = 1
                    elif num == 3:
                        now = 1
                        leak = 1

                else:
                    num = a[index_a] + b[index_b] + leak
                    if num == 0 or num == 1:
                        now = num
                        leak = None
                    elif num == 2:
                        now = 0
                        leak = 1
                    elif num == 3:
                        now = 1
                        leak = 1

            return_list.append(now)
            index_a -= 1
            index_b -= 1
        
        return_list.reverse()
        last = "".join(return_list)
        return(last)