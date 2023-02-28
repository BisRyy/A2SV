class Solution:
	def find132pattern(self, nums: List[int]) -> bool:
		mid = -float('inf')
		stack = []
		for i in nums[::-1]:
			if i < mid:
				return 1
			while stack and stack[-1] < i:
				mid = stack.pop()
			stack.append(i)
		return 0
