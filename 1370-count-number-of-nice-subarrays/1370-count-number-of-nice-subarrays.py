class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left,middle,count,res = 0,0,0,0
        for right in range(len(nums)):
            if nums[right] % 2 != 0: # if it is odd
                count += 1
            while count > k:
                if nums[left] % 2 != 0:
                    count -= 1
                left += 1
                middle = left
            if count == k:
                while nums[middle] % 2 == 0:
                    middle += 1
                res += middle - left + 1

        return res
