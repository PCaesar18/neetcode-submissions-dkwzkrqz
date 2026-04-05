class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # We need to return all ways to split s into valid dictionary words.
        # At each index, try every possible end position.
        # If s[i:j] is a valid word, recursively solve the suffix from j.
        # Use a set for fast lookup and memoize by index so we do not
        # recompute the same suffix many times.
        
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def backtrack(index):
            result = []
            if index in memo:
                return memo[index]
            if index == n:
                 # to add words 
                return [""]

            for end in range(index + 1, n + 1):
                if s[index:end] in wordSet:
                    suffixes = backtrack(end)
                    for suffix in suffixes:
                        if suffix == "":
                            result.append(s[index:end])
                        else:
                            result.append(s[index:end] + " " + suffix)
            memo[index] = result
            return result
        return backtrack(0)                



    #again we create a function whether it is valid the splits, we could use a sliding window technique?