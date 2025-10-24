class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        ans = 0

        left, right = 0,0
        
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

            right += 1

        return ans

        