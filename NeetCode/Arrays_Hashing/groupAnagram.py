class Solution:
    def groupAnagrams(self, strs):
        mapp = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in mapp:
                mapp[sorted_word].append(word)
            else:
                mapp[sorted_word] = [word]
        return list(mapp.values())

f = ["act","pots","tops","cat","stop","hat"]

print(Solution().groupAnagrams(f))
