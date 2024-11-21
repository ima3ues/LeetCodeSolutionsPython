# Easy
# 412 Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Base Code
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
 
# Solution
class Solution(object):
    def fizzBuzz(self, n):
        string_array = [None] * (n)
        index = 0
        for i in range(n):
            index += 1
            if (index % 3 == 0 and index % 5 == 0):
                string_array[i] = "FizzBuzz"
            elif index % 3 == 0:
                string_array[i] = "Fizz"
            elif index % 5 == 0:
                string_array[i] = "Buzz"
            else: 
                string_array[i] = str(index)
        return string_array