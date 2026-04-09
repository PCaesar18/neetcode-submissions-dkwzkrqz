class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we get to pick/choose k (banana per hour eating rate)
        # return min k to eat all bananas within h hours 
        upper = max(piles)
        lower = 1 
        result = upper

        while lower <= upper:
            mid = (lower + upper) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid #math.ceil(pile / mid) #
            if hours <= h:
                result = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return result 

        