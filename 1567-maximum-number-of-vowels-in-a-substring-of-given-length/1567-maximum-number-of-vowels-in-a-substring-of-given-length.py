class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        vowel_count = 0

        for char in s[:k]:
            if char in vowel:
                vowel_count += 1

        ans = vowel_count
        left, right = 0,k

        while right < len(s):

            if s[right] in vowel:
                vowel_count += 1
            
            if s[left] in vowel:
                vowel_count -= 1

            ans = max(ans, vowel_count)

            left += 1
            right += 1
        
        return ans
            

            