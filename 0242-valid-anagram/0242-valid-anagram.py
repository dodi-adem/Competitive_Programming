class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS = defaultdict(int)

        for char in s:
            hashS[char] += 1

        for char in t:
            hashS[char] -= 1

            if hashS[char] < 0:
                return False
        return True    