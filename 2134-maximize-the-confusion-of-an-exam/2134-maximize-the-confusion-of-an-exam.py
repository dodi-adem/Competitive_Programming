class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def answer(letter):
            left = 0
            count = 0
            maxi = 0

            for right in range(len(answerKey)):
                if answerKey[right] != letter:
                    count += 1
                while count > k:
                    if answerKey[left] != letter:
                        count -= 1
                    left += 1
                maxi = max(maxi, right - left + 1)

            return maxi

        return max(answer('T'), answer('F'))    
        