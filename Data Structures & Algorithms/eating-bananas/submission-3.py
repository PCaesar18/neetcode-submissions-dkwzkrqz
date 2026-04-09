class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we get to pick/choose k (banana per hour eating rate)
        # return min k to eat all bananas within h hours 
        upper = max(piles)
        lower = 1 
        result = upper

        while lower <= upper:
            mid = (lower + upper) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime <= h:
                result = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return result 

        