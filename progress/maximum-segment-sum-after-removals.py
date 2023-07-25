class UF(object):
    def __init__(self, nums):
        self.parent = [-num for num in nums]
        self.size = [1 for _ in range(len(nums))]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        valP = self.parent[rootP]
        valQ = self.parent[rootQ]

        if rootP == rootQ:
            return
        if (self.size[rootP] > self.size[rootQ]):
            self.parent[rootQ] = rootP
            self.parent[rootP] = valP + valQ
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.parent[rootQ] = valP + valQ
            self.size[rootQ] += self.size[rootP]

    def find(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x
    
    def getval(self, index):
        root = self.find(index)
        return -self.parent[root]

class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        res = []
        curr_max = 0
        temp = [-1 for _ in range(len(nums))]
        uf = UF(nums[:])
        
        for index in removeQueries[::-1]:
            res.append(curr_max)
            temp[index] = nums[index]

            if index > 0 and temp[index-1] > 0:
                uf.union(index, index-1)
            if index < len(nums) - 1 and temp[index+1] > 0:
                uf.union(index, index+1)
            curr_max = max(curr_max, uf.getval(index))
            
        return res[::-1]
