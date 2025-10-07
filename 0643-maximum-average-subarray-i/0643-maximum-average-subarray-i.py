class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        best = summ/k
        left = 0
        right = k
        while right < len(nums):
            summ =  summ + nums[right] - nums[left]
            best = max(best,summ/k)
            left += 1
            right += 1
        
        return best