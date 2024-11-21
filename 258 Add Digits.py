# Easy 
# 258 Add Digits 
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Base Code
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

# Solution
class Solution(object):
    def addDigits(self, num): # O(1), define a function doesn't contribute to execution time
        """
        Time Complexity: O(log n)
        as counted in the inline it should be O(k log log k)
        as k = log n, as in the code k represent the number of digits, and mathematically k = log n + 1, where in Big O we will ignore constant
        ttl time complexity = O(log n * log log log n), while log log log n is too small where we can assume it as O(1), and it will be O(log n) only
        """
        sumOfEachDigit = num # O(1), initialize any variables takes the same amount of time
        check_num = num # O(1), initialize any variables takes the same amount of time
        
        while len(str(check_num)) > 1: # O(k log log k) in the ReadMe
        # time complexity of str(check_num) is O(k), where k is the number of digits being converted
        # time complexity of len(str(check_num)) is O(1) as retrieve any value's length takes the same amount of time
        # time complexity of >1 is O(1) 
        # ttl time complexity per condition evaluation is O(k) + O(1) + O(1) = O(k) -> Occurs once per iteration
        # time complexity per iteration is O(k) + O(1) + O(k) + O(1) = O(2k) = O(k)
        # time complexity over all iteration is O(log log k) * O(k) = O(k log log k), O(log log k) is the number of iterations

            sumOfEachDigit = 0 # O(1), initialize any variables takes the same amount of time

            for each_char in str(check_num): # O(k) in the ReadMe
            # time complexity per iteration is O(1) + O(1) = O(1)
            # time complexity over all iteration is k * O(1) = O(k), k is the number of iteration

                current = int(each_char) # O(1), initialize any variables takes the same amount of time
                # originally the time complexity of int(each_char) should be O(k), where k is the length of the string being converted,
                # however, as we know that each_char is a single character from the string check_num, therefore each_char is a string of length 1, which leads to O(1)

                sumOfEachDigit += current # O(1), adding any two numbers within a fixed size takes the same amount of time
            
            check_num = sumOfEachDigit # O(1), assigning any variables takes the same amount of time
       
        return sumOfEachDigit