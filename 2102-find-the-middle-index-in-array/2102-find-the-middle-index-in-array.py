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

        # this is the effcient way(space complexity = o(1)) i get from youtube

        # total_sum = sum(nums)
        # left_sum = 0
        # for i,num in enumerate(nums):
        #     if left_sum == total_sum - left_sum - num:
        #         return i
        #     left_sum += num
        
        # return -1