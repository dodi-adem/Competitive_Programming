class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lst:
                return [lst[complement],i]
            lst[nums[i]] = i
        