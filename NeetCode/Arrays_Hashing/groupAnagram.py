from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mapp = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            mapp[sorted_word].append(word)
        return list(mapp.values())

f = ["act","pots","tops","cat","stop","hat"]

print(Solution().groupAnagrams(f))

# Time Complexity: O(k * n log n)
# Space Complexity: O(n * k)