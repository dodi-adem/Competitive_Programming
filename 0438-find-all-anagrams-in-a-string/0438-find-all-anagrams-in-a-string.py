class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = sorted(p)
        window = s[:len(p)]
        res = list()
        if sorted(window) == check:
            res.append(0)
        left = 1
        right = len(p)
        while right < len(s):
            if sorted(s[left:right+1]) == check:
                res.append(left)
            left += 1
            right += 1

        return res