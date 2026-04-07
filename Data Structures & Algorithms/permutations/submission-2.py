class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for num in nums:
                if num in used:
                    continue
                perm.append(num)
                used.add(num)
                backtrack(perm)
                perm.pop()
                used.remove(num)

        backtrack([])
        return result 

        