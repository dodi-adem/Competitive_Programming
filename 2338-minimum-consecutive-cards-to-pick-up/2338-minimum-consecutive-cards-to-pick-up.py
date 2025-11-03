class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')
        seen = {} # val : index

        for index, val in enumerate(cards):
            if val in seen:
                res = min(res,index - seen[val] + 1)
            seen[val] = index
        
        return res if res != float('inf') else -1