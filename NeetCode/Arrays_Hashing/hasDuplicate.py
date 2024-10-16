class Solution:
	def hasDuplicate(self, nums):
		return not (len(set(nums)) == len(nums))

nums = [1, 2, 3, 1]
print(Solution().hasDuplicate(nums))

# Time comp : O(n)
# Space comp : O(n)