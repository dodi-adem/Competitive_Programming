class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = Counter(p)
        window = s[:len(p)]
        res = list()

        if Counter(window) == check:
            res.append(0)
        
        left = 1
        right = len(p)

        while right < len(s):
            if Counter(s[left:right+1]) == check:
                res.append(left)
            left += 1
            right += 1
        
        return res