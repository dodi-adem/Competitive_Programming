class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 0
        prefixsum = nums[0]
        for i in range(1,n):
            prefix[i] = prefixsum
            prefixsum += nums[i]
        
        suffix = [0] * n
        suffix[n-1] = 0
        suffixsum = nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffixsum
            suffixsum += nums[i]

        for i in range(n):
            if prefix[i] == suffix[i]:
                return i

        return -1