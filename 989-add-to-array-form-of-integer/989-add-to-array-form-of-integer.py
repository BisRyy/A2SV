class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(a) for a in num]
        return [int(a) for a in list(str(int("".join(num)) + k))]