class Solution:
	def isAnagram(self, s, t):
		if len(s) != len(t):
			return False
		return sorted(s) == sorted(t)
	
print(Solution().isAnagram("jam", "jar"))

# Time Complexity: O(n log n)
# Space Complexity: O(1)