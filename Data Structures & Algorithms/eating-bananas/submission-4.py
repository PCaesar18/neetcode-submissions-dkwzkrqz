class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we get to pick/choose k (banana per hour eating rate)
        # return min k to eat all bananas within h hours 
        upper = max(piles) #upper bound is what can be eaten in one go
        lower = 1 #min speed is 1, not 0 because cannot division by 0
        result = upper

        while lower <= upper:
            mid = (lower + upper) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid) # we have to round up so normal division is not correct 
            if totalTime <= h:
                result = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return result 

        