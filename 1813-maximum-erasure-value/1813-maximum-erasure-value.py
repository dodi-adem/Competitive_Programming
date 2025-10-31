class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res,add = 0,0
        seen = set()
        left = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                add -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            add += nums[right]
            res = max(res,add)

                
        return res
        