class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        add = 0
        left = 0

        for right in range(len(nums)):
            add += nums[right]
            while add >= target:
                res = min(res,right-left+1)
                add -= nums[left]
                left += 1

        return 0 if res == float('inf') else res
        