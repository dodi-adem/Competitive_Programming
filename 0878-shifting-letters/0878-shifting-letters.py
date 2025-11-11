class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        res = ''
        suffix = [0] * n
        suffixsum = shifts[-1] % 26
        suffix[-1] = suffixsum
        for i in range(n - 2,-1,-1):
            suffix[i] = (shifts[i] + suffixsum) % 26
            suffixsum = suffix[i]
        for i in range(len(s)):
            shifted = (ord(s[i]) - ord('a') + suffix[i]) % 26
            res += chr(shifted + ord('a'))

        return res

