class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False] * len(nums)
        def backtrack(subset):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: 
                    continue

                subset.append(nums[i])
                used[i] = True
                backtrack(subset)
                subset.pop()
                used[i] = False
        backtrack([])
        return result 
                
            


        