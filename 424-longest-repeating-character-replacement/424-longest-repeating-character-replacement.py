class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0

        for letter in set(s):
            left = 0
            count = 0

            for right in range(len(s)):
                if s[right] == letter:
                    count += 1

                while not right + 1 - left - count <= k:
                    if s[left] == letter:
                        count -= 1
                    left += 1

                answer = max(answer, right + 1 - left)

        return answer