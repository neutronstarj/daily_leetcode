class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set min to inf, set max to be 0 , we are doing backward 
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price<min_price:
                min_price = price
            elif price -min_price >max_profit :
                max_profit = price - min_price
        return max_profit 


        
