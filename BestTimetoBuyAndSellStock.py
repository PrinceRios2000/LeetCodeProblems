class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [7,1,5,3,6,4], maxProfit = 0
        
        max=0
        curr_small=7
        
        '''
        max_profit = 0
        curr_smallest = prices[0]

        for i in range(1, len(prices)):
            diff = prices[i] - curr_smallest
            if diff > max_profit:
                max_profit = diff
            curr_smallest = min(curr_smallest, prices[i])
        
        return max_profit