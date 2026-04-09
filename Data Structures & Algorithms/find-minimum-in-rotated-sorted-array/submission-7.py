class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n -1 

        while l < r:
            mid = (l + r) // 2
            #optional if normal non rotated
            # if nums[l] < nums[r]:
                #return nums[l]
            if nums[mid] > nums[r]:
                l = mid + 1

            if nums[mid] <= nums[r]:
                r = mid
            
        return nums[l] #return nums[l] because we have to return the minimum 