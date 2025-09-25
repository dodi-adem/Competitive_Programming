class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left , right = 0 , 0
        best = 0
        while right < len(s):
            while s[right] in seen:      
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            best = max(best,right - left )
        return best