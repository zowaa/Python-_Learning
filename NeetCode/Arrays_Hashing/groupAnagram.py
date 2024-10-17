class Solution:
    def groupAnagrams(self, strs):
        mapp = {}
        for word in strs:
            added= False
            for key,val in mapp.items():
                if (len(key) == len(word)) and (sorted(key) == sorted(word)):
                    val.append(word)
                    added = True
            else:
                if not added:
                    mapp[word] = [word]
        return list(mapp.values())

f = ["act","pots","tops","cat","stop","hat"]

print(Solution().groupAnagrams(f))