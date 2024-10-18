class Solution:
	# def twoSum(self,nums,target):
	# 	for i in range(len(nums)-1):
	# 		for j in range(i+1, len(nums)):
	# 			if nums[i] + nums[j] == target:
	# 				return [i,j]

	def twoSum(self,nums,target):
		hash_map = {}
		for n in range(len(nums)):
			rem = target - nums[n]
			if rem in hash_map:
				return [hash_map[rem],n]
			hash_map[nums[n]] = n

				
print(Solution().twoSum([4,5,6],10))

# Time Complexity: O(n)
# Space Complexity: O(n)