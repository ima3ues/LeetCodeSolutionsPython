# Easy
# 1672 Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Base Code
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

# Solution
class Solution(object):
    def maximumWealth(self, accounts):
        for account in accounts:
            ttl_money = 0
            for money in account:
                ttl_money += money
            prev_money = 0
            if ttl_money >= prev_money:
                wealth = ttl_money
                prev_money = ttl_money
            else:
                wealth = prev_money

        return wealth  
        
