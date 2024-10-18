from collections import defaultdict

class Solution:
	def topKFrequent(self, nums, k):
		fq = defaultdict(int)
		for n in nums:
			fq[n] +=1

		res = []
		for n, val in fq.items():
			res.append([val, n])
		res.sort()

		final = []
		for i in range(0, k):
			final.append(res.pop()[1])
			
		return final

nums = [1,1,2,3,3,3]
print(Solution().topKFrequent(nums, 2))