class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        llst = {}
        for i,num in enumerate(nums):
            if num in llst:
                dist = i - llst[num]
                if dist <= k:
                    return True
            llst[num] = i

        return False


        