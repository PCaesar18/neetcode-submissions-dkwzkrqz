class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, subset):
            if start == n:
                result.append(subset.copy())
                return
            
            for end in range(start, n):
                if isPalindrome(start,end):
                    subset.append(s[start:end + 1]) # + 1 because left inclusive and right exclusive slicing
                    backtrack(end + 1, subset)
                    subset.pop()

        backtrack(0,[])
        return result 

        