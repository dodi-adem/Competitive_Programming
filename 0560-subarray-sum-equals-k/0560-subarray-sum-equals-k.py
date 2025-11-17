class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0
        prefix_count = {0:1}

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k

            if target in prefix_count:
                result += prefix_count[target]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return result
