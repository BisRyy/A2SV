class Solution:
	def numDecodings(self, s: str) -> int:
		if(s[0] == '0'):
			return 0
		if(len(s) == 1):
			return 1
		
		
		count1, count2 = 1, 1
		for i in range(1, len(s)):
			d = int(s[i])
			dd = int(s[i-1] + s[i]) 
			
			count = 0 
            
			if(d > 0):
				count+=count2
				
			if(dd>=10 and dd<=26):
				count+=count1

			count1 = count2
			count2 = count
	
		return count2