class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = {}
        r = []
        for i, s in enumerate(strs):
            t = sorted(s)
            t = "".join(t)
            if t not in key:
                r.append([s])
                key[t] = len(key)
            else:
                r[key.get(t)].append(s)
        return r