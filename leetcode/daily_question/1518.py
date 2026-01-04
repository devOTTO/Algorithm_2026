class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        full = numBottles
        total = 0
        flag = True
        
        while flag:
            #drink
            total += full 
            empty += full
            full = 0

            # exchange
            full = empty // numExchange

            if full == 0:
                break
            empty -= full * numExchange

        return total
