class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False
        check = Counter(s1)
        window = s2[:len1]
        count = Counter(window)
        if check == count:
            return True
        left = 0

        for right in range(len1, len2):
            count[s2[right]] += 1
            count[s2[left]] -= 1
            if count[s2[left]] == 0:
                del count[s2[left]] 
            
            if count == check:
                return True
            
            left += 1
        
        return False
