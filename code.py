class Solution:
    def maximumProfit(self, prices):
        # code here
        
        maxEarn = 0
        lowest = prices[0]
        
        for i in range(1,len(prices)):
            earn = prices[i] -lowest
            if earn > maxEarn:
                maxEarn = earn
            if prices[i] < lowest:
                lowest = prices[i]
                
        return maxEarn