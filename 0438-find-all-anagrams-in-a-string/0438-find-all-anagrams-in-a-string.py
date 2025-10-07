class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        res = []
        check = Counter(p)
        window = s[:len(p)]
        freq = Counter(window)
        if freq == check:
            res.append(0)
        left = 0
        right = len(p)

        while right < len(s):
            freq[s[right]] += 1
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]
            
            if freq == check:
                res.append(left+1)
            
            left += 1
            right += 1

        return res
