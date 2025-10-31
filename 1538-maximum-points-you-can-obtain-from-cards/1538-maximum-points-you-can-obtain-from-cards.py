class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        left , right = 0 , len(cardPoints) - k

        total = sum(cardPoints[:right])
        res = totalSum - total

        while right < len(cardPoints):
            total += cardPoints[right] - cardPoints[left]
            res = max(res,totalSum - total)
            left += 1
            right += 1

        return res