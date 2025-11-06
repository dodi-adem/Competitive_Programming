class Solution:
    def balancedString(self, s: str) -> int:
        res = float("inf")
        target = len(s)/4
        count = Counter(s)
        left = 0

        if max(count.values()) == target:
            return 0

        for right in range(len(s)):
            count[s[right]] -= 1

            while left <= right and max(count.values()) <= target:
                res = min(res,right - left + 1)
                count[s[left]] += 1
                left += 1

        return res

            